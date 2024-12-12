


 


SimpleVADModule
===============

.. py:module:: simple_vad

.. autoapi-nested-parse::

   SimpleVADModule
   ===============

   A retico module that provides Voice Activity Detection (VAD) using
   WebRTC's VAD. Takes AudioIU as input, resamples the IU's raw_audio to
   match WebRTC VAD's input frame rate, then call the VAD to predict
   (user's) voice activity on the resampled raw_audio (True == speech
   recognized), and finally returns the prediction alognside with the
   raw_audio (and related parameter such as frame rate, etc) using a new IU
   type called VADIU.

   It also takes TextIU as input, to additionally keep tracks of the
   agent's voice activity (agent == the retico system) by receiving IUs
   from the SpeakerModule. The agent's voice activity is also outputted in
   the VADIU.

   Inputs : AudioIU, TextIU

   Outputs : VADIU




Classes
-------

.. autoapisummary::

   simple_retico_agent.simple_vad.SimpleVADModule


Module Contents
---------------

.. py:class:: SimpleVADModule(target_framerate=16000, input_framerate=44100, channels=1, sample_width=2, vad_aggressiveness=3, **kwargs)

   Bases: :py:obj:`retico_core.AbstractModule`


   A retico module that provides Voice Activity Detection (VAD) using
   WebRTC's VAD. Takes AudioIU as input, resamples the IU's raw_audio to match
   WebRTC VAD's input frame rate, then call the VAD to predict (user's) voice
   activity on the resampled raw_audio (True == speech recognized), and
   finally returns the prediction alognside with the raw_audio (and related
   parameter such as frame rate, etc) using a new IU type called VADIU.

   It also takes TextIU as input, to additionally keep tracks of the
   agent's voice activity (agent == the retico system) by receiving IUs
   from the SpeakerModule. The agent's voice activity is also outputted
   in the VADIU.

   Initializes the SimpleVADModule Module.

   :param target_framerate: framerate of the output
                            VADIUs (after resampling). Defaults to 16000.
   :type target_framerate: int, optional
   :param input_framerate: framerate of the received
                           AudioIUs. Defaults to 44100.
   :type input_framerate: int, optional
   :param channels: number of channels (1=mono,
                    2=stereo) of the received AudioIUs. Defaults to 1.
   :type channels: int, optional
   :param sample_width: sample width (number of bits
                        used to encode each frame) of the received AudioIUs.
                        Defaults to 2.
   :type sample_width: int, optional
   :param vad_aggressiveness: The level of
                              aggressiveness of VAD model, the greater the more
                              reactive. Defaults to 3.
   :type vad_aggressiveness: int, optional


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



   .. py:method:: resample_audio(raw_audio)

      Resample the audio's frame_rate to correspond to
      self.target_framerate.

      :param raw_audio: the audio received from the microphone that
                        could need resampling.
      :type raw_audio: bytes

      :returns: the resampled audio chunk.
      :rtype: bytes



   .. py:method:: process_update(update_message)

      Receives TextIU and AudioIU, use the first one to set the
      self.VA_agent class attribute, and process the second one by predicting
      whether it contains speech or not to set VA_user IU parameter.

      :param update_message: UpdateMessage that contains new
                             IUs (TextIUs or AudioIUs), both are used to provide
                             voice activity information (respectively for agent and
                             user).
      :type update_message: UpdateType



