"""
SpeakerModule_Interruption
==================

This module outputs the audio signal contained in the AudioIUs by the computer's speakers,
and can interrupt this audio streaming if the user starts speaking (with the reception of VADStateIUs).
"""

import datetime
import threading
import time
import pyaudio
import retico_core
import platform
import retico_core.abstract
from retico_core.audio import AudioIU, SpeakerModule
from utils import *

from utils import *
from vad import VADStateIU
from vad_turn import AudioVADIU


class SpeakerInterruptionModule(retico_core.AbstractConsumingModule):
    """A module that consumes AudioIUs of arbitrary size and outputs them to the
    speakers of the machine. It stops outputting audio if the user starts speaking,
    because it also receives information trough the VADStateIU.
    When a new IU is incoming, the module blocks as long as the current IU is being played.
    """

    @staticmethod
    def name():
        return "Speaker Interruption Module"

    @staticmethod
    def description():
        return "A consuming module that plays audio from speakers and stops playing audio if the user starts speaking (it receives a VADStateIU == True)"

    @staticmethod
    def input_ius():
        return [AudioIU, AudioVADIU]

    @staticmethod
    def output_iu():
        return None

    def __init__(
        self,
        rate=44100,
        frame_length=0.2,
        sample_width=2,
        channels=1,
        use_speaker="both",
        device_index=None,
        log_file="speaker_interruption.csv",
        log_folder="logs/test/16k/Recording (1)/demo",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.rate = rate
        self.sample_width = sample_width
        self.use_speaker = use_speaker

        self._p = pyaudio.PyAudio()

        if device_index is None:
            device_index = self._p.get_default_output_device_info()["index"]
        self.device_index = device_index

        self.stream = None
        self.time = None

        self.channels = channels
        self.log_file = manage_log_folder(log_folder, log_file)
        self.time_logs_buffer = []
        self.first_time = True

        # interruptions parameters
        self.vad_state = False
        self.audio_buffer = []
        self.audioIU_buffer = []
        self.old_iu = None
        self.frame_length = frame_length

    def process_update(self, update_message):
        """overrides SpeakerModule : https://github.com/retico-team/retico-core/blob/main/retico_core/audio.py#L282

        overrides SpeakerModule's process_update to save logs.
        """
        # TODO: replace this method by an actual way of knowing what is the starting and ending time where the speaker is active (actually outputs time, and not receive messages).
        if self.first_time:
            self.time_logs_buffer.append(
                ["Start", datetime.datetime.now().strftime("%T.%f")[:-3]]
            )
            self.first_time = False
        else:
            self.time_logs_buffer.append(
                ["Stop", datetime.datetime.now().strftime("%T.%f")[:-3]]
            )
        for iu, ut in update_message:
            if isinstance(iu, AudioVADIU):
                if ut == retico_core.UpdateType.ADD:
                    if iu.vad_state == "interruption":
                        # user starts talking, set vad_state to false to interrupt the audio output
                        self.vad_state = True

                        print("Someone starts talking, speakers stops playing audio")

                        # Last IU in audioBuffer :
                        if len(self.audioIU_buffer) != 0:
                            prev_iu = self.audioIU_buffer[-1].grounded_in
                            print(
                                "last IU.grounded_in = ",
                                prev_iu,
                            )
                            prev_ius = []
                            while prev_iu.previous_iu is not None:
                                prev_iu = prev_iu.previous_iu
                                prev_ius.append(prev_iu.payload)
                            prev_ius.reverse()
                            print(
                                "LAST AudioVADIU = ",
                                "".join(prev_ius),
                            )

                        # First IU in audioBuffer :
                        if len(self.audioIU_buffer) != 0:
                            prev_iu = self.audioIU_buffer[0].grounded_in
                            print(
                                "first IU.grounded_in = ",
                                prev_iu,
                            )
                            prev_ius = []
                            while prev_iu.previous_iu is not None:
                                prev_iu = prev_iu.previous_iu
                                prev_ius.append(prev_iu.payload)
                            prev_ius.reverse()
                            print(
                                "FIRST AudioVADIU = ",
                                "".join(prev_ius),
                            )
                if ut == retico_core.UpdateType.COMMIT:
                    if iu.vad_state == "user_turn":
                        # user stoped talking, set vad_state to true because speaker can receive new audio from next user turn
                        # print("user stoped talking")
                        self.vad_state = False
                        self.audio_buffer = []
                        self.audioIU_buffer = []
            elif isinstance(iu, AudioIU):
                if ut == retico_core.UpdateType.ADD:
                    # if true, interruption is occuring
                    if self.vad_state:
                        self.old_iu = iu
                        # print("SPEAKER : Interruption occuring")
                        # TODO : REVOKE so that it REVOKES IUs of TTS and LLM to align dialogue history with the interruption of speaker
                        # print("iu.grounded_in : ", iu.grounded_in)
                        prev_iu = iu.grounded_in
                        prev_ius = []
                        while prev_iu.previous_iu is not None:
                            # print("prev_iu : ", prev_iu.previous_iu)
                            prev_iu = prev_iu.previous_iu
                            prev_ius.append(prev_iu.payload)
                        prev_ius.reverse()
                        print(
                            "AudioIU = ",
                            "".join(prev_ius),
                        )
                        # print(
                        #     "iu.grounded_in.grounded_in : ", iu.grounded_in.grounded_in
                        # )
                    else:
                        if self.old_iu is not None and self.old_iu == iu.previous_iu:
                            # print(
                            #     "SPEAKER : IU is the end of the interrupted turn.",
                            #     self.old_iu,
                            # )
                            self.old_iu = iu
                            # TODO : REVOKE so that it REVOKES IUs of TTS and LLM to align dialogue history with the interruption of speaker
                            # print("iu.grounded_in : ", iu.grounded_in)
                            # print(
                            #     "iu.grounded_in.grounded_in : ",
                            #     iu.grounded_in.grounded_in,
                            # )
                        else:
                            # print("SPEAKER : ADD AUDIO to buffer")
                            self.audio_buffer.append(bytes(iu.raw_audio))
                            self.audioIU_buffer.append(iu)
                    # if not self.vad_state and self.old_iu != iu.previous_iu:
                    #     # if self.old_iu != iu.previous_iu:
                    #     # if not self.vad_state:
                    #     self.audio_buffer.append(bytes(iu.raw_audio))
                    # else:
                    #     self.old_iu = iu
            else:
                # raise Exception("Unknown IU type " + iu)
                # raise NotImplementedError("Unknown IU type " + iu)
                raise TypeError("Unknown IU type " + iu)

        return None

    def callback(self, in_data, frame_count, time_info, status):
        if len(self.audio_buffer) == 0:
            silence_bytes = b"\x00" * frame_count * self.channels * self.sample_width
            return (silence_bytes, pyaudio.paContinue)
        data = self.audio_buffer.pop()
        self.audioIU_buffer.pop()
        return (data, pyaudio.paContinue)

    def setup(self):
        """overrides SpeakerModule : https://github.com/retico-team/retico-core/blob/main/retico_core/audio.py#L288"""
        return

    def prepare_run(self):
        """overrides SpeakerModule : https://github.com/retico-team/retico-core/blob/main/retico_core/audio.py#L288"""

        p = self._p

        if platform.system() == "Darwin":
            if self.use_speaker == "left":
                stream_info = pyaudio.PaMacCoreStreamInfo(channel_map=(0, -1))
            elif self.use_speaker == "right":
                stream_info = pyaudio.PaMacCoreStreamInfo(channel_map=(-1, 0))
            else:
                stream_info = pyaudio.PaMacCoreStreamInfo(channel_map=(0, 0))
        else:
            stream_info = None

        # Adding the stream_callback parameter should make the stream.write() function non blocking,
        # which would make it possible to run in parallel of the reception of update messages (and the uptdate of vad_state)
        self.stream = p.open(
            format=p.get_format_from_width(self.sample_width),
            channels=self.channels,
            rate=self.rate,
            input=False,
            output_host_api_specific_stream_info=stream_info,
            output=True,
            output_device_index=self.device_index,
            stream_callback=self.callback,
            frames_per_buffer=int(self.rate * self.frame_length),
        )

        self.stream.start_stream()

    def shutdown(self):
        """overrides SpeakerModule : https://github.com/retico-team/retico-core/blob/main/retico_core/audio.py#L312

        Write logs and close the audio stream."""
        write_logs(
            self.log_file,
            self.time_logs_buffer,
        )
        self.stream.stop_stream()
        self.stream.close()
        self.stream = None
