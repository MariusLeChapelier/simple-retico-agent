


 


SimpleSpeakerModule
===================

.. py:module:: simple_speaker

.. autoapi-nested-parse::

   SimpleSpeakerModule
   ===================

   A retico module that outputs through the computer's speakers the audio
   contained in AudioFinalIU. The module is similar to the original
   SpeakerModule, except it outputs TextIU when an agent Begining-Of-Turn
   or End-Of-Turn is encountered. I.e. when it outputs the audio of,
   respectively, the first and last AudioIU of an agent turn (information
   calculated from latest_processed_iu and IU's final attribute). These
   agent BOT and EOT information could be received by a Voice Activity
   Dectection (VAD) or a Dialogue Manager (DM) Modules.

   Inputs : AudioFinalIU

   Outputs : TextIU




Classes
-------

.. autoapisummary::

   simple_retico_agent.simple_speaker.SimpleSpeakerModule


Module Contents
---------------

.. py:class:: SimpleSpeakerModule(rate=44100, frame_length=0.2, channels=1, sample_width=2, use_speaker='both', device_index=None, **kwargs)

   Bases: :py:obj:`retico_core.AbstractModule`


   A retico module that outputs through the computer's speakers the audio
   contained in AudioFinalIU. The module is similar to the original
   SpeakerModule, except it outputs TextIU when an agent Begining-Of-Turn or
   End-Of-Turn is encountered. I.e. when it outputs the audio of,
   respectively, the first and last AudioIU of an agent turn (information
   calculated from latest_processed_iu and IU's final attribute). These agent
   BOT and EOT information could be received by a Voice Activity Dectection
   (VAD) or a Dialogue Manager (DM) Modules.

   Inputs : AudioFinalIU

   Outputs : TextIU

   Initializes the SimpleSpeakerModule.

   :param rate: framerate of the played audio chunks.
   :type rate: int
   :param frame_length: duration of the played audio chunks.
   :type frame_length: float
   :param channels: number of channels (1=mono, 2=stereo) of the
                    received AudioFinalIU.
   :type channels: int
   :param sample_width: sample width (number of bits used to
                        encode each frame) of the received AudioFinalIU.
   :type sample_width: int
   :param use_speaker: wether the audio should be played in
                       the right, left or both speakers.
   :type use_speaker: string
   :param device_index: PortAudio's default device.
   :type device_index: string


   .. py:method:: name()
      :staticmethod:


      Return the human-readable name of the module.

      :returns: A string containing the name of the module
      :rtype: str



   .. py:method:: description()
      :staticmethod:


      Return the human-readable description of the module.

      :returns: A string containing the description of the module
      :rtype: str



   .. py:method:: input_ius()
      :staticmethod:


      Return the list of IU classes that may be processed by this module.

      If an IU is passed to the module that is not in this list or a subclass
      of this list, an error is thrown when trying to process that IU.

      :returns: A list of classes that this module is able to process.
      :rtype: list



   .. py:method:: output_iu()
      :staticmethod:


      Return the class of IU that this module is producing.

      :returns: The class of IU this module is producing.
      :rtype: class



   .. py:method:: process_update(update_message)

      Process the received ADD AudioFinalIU by storing them in
      self.audio_iu_buffer.



   .. py:method:: callback(in_data, frame_count, time_info, status)

      Callback function given to the pyaudio stream that will output audio
      to the computer speakers. This function returns an audio chunk that
      will be written in the stream. It is called everytime the last chunk
      has been fully consumed.

      :param in_data:
      :type in_data: _type_
      :param frame_count: number of frames in an audio chunk
                          written in the stream.
      :type frame_count: int
      :param time_info:
      :type time_info: _type_
      :param status:
      :type status: _type_

      :returns:

                the tuple containing the audio chunks
                    (bytes) and the pyaudio type informing wether the stream
                    should continue or stop.
      :rtype: (bytes, pyaudio type)



   .. py:method:: prepare_run()

      Open the stream to enable sound outputting through speakers.



   .. py:method:: shutdown()

      Close the audio stream.



