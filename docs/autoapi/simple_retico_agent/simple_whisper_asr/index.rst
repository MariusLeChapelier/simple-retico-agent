


 


SimpleWhisperASRModule
======================

.. py:module:: simple_whisper_asr

.. autoapi-nested-parse::

   SimpleWhisperASRModule
   ======================

   A retico module that provides Automatic Speech Recognition (ASR) using a
   OpenAI's Whisper model.

   Once the user starts talking, periodically predicts a new transcription
   hypothesis from the incremental speech received, and sends the new words
   as SpeechRecognitionIUs (with UpdateType = ADD). The incorrect words
   from last hypothesis are REVOKED.  When the user stops talking, predicts
   a final hypothesis and sends the corresponding IUs (with UpdateType =
   COMMIT).

   The faster_whisper library is used to speed up the whisper inference.

   Inputs : VADTurnAudioIU

   Outputs : SpeechRecognitionIU




Classes
-------

.. autoapisummary::

   simple_retico_agent.simple_whisper_asr.SimpleWhisperASRModule


Module Contents
---------------

.. py:class:: SimpleWhisperASRModule(whisper_model='distil-large-v2', device=None, framerate=16000, silence_dur=1, silence_threshold=0.75, bot_dur=0.4, bot_threshold=0.75, **kwargs)

   Bases: :py:obj:`retico_core.AbstractModule`


   A retico module that provides Automatic Speech Recognition (ASR) using a
   OpenAI's Whisper model.

   Once the user starts talking, periodically predicts a new
   transcription hypothesis from the incremental speech received, and
   sends the new words as SpeechRecognitionIUs (with UpdateType = ADD).
   The incorrect words from last hypothesis are REVOKED.  When the user
   stops talking, predicts a final hypothesis and sends the
   corresponding IUs (with UpdateType = COMMIT).

   The faster_whisper library is used to speed up the whisper
   inference.

   Inputs : VADTurnAudioIU

   Outputs : SpeechRecognitionTurnIU

   Initializes the SimpleWhisperASRModule Module.

   :param whisper_model: name of the desired model,
                         has to correspond to a model in the faster_whisper
                         library. Defaults to "distil-large-v2".
   :type whisper_model: str, optional
   :param device: wether the model will be executed
                  on cpu or gpu (using "cuda"). Defaults to None.
   :type device: _type_, optional
   :param framerate: framerate of the received VADIUs.
                     Defaults to 16000.
   :type framerate: int, optional
   :param silence_dur: Duration of the time interval
                       over which the user's EOT will be calculated. Defaults
                       to 1.
   :type silence_dur: int, optional
   :param silence_threshold: share of IUs in the
                             last silence_dur seconds to present negative VA to
                             predict user EOT. Defaults to 0.75.
   :type silence_threshold: float, optional
   :param bot_dur: Duration of the time interval
                   over which the user's BOT will be calculated. Defaults
                   to 0.4.
   :type bot_dur: float, optional
   :param bot_threshold: share of IUs in the last
                         bot_dur seconds to present positive VA to predict user
                         BOT. Defaults to 0.75.
   :type bot_threshold: float, optional


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



   .. py:method:: get_n_audio_chunks(n_chunks_param_name, duration)

      Returns the number of audio chunks corresponding to duration. Stores
      this number in the n_chunks_param_name class argument if it hasn't been
      done before.

      :param n_chunks_param_name: the name of class argument to
                                  check and/or set.
      :type n_chunks_param_name: str
      :param duration: duration in second.
      :type duration: float

      :returns: the number of audio chunks corresponding to duration.
      :rtype: int



   .. py:method:: recognize_user_bot()

      Return the prediction on user BOT from the current audio buffer.
      Returns True if enough audio chunks contain speech.

      :returns: the BOT prediction.
      :rtype: bool



   .. py:method:: recognize_user_eot()

      Return the prediction on user EOT from the current audio buffer.
      Returns True if enough audio chunks do not contain speech.

      :returns: the EOT prediction.
      :rtype: bool



   .. py:method:: recognize_agent_bot()

      Return True if the last VAIU received presents a positive agent VA.

      :returns: the BOT prediction.
      :rtype: bool



   .. py:method:: recognize_agent_eot()

      Return True if the last VAIU received presents a negative agent VA.

      :returns: the EOT prediction.
      :rtype: bool



   .. py:method:: recognize_turn(_n_audio_chunks=None, threshold=None, condition=None)

      Function that predicts user BOT/EOT from VADIUs received.

      Example : if self.silence_threshold==0.75 (percentage) and
      self.bot_dur==0.4 (seconds), It predicts user BOT (returns True)
      if, across the frames corresponding to the last 400ms second of
      audio, >75% contains speech.

      :param _n_audio_chunks: the threshold number of
                              audio chunks to recognize a user BOT or EOT. Defaults to
                              None.
      :type _n_audio_chunks: _type_, optional
      :param threshold: the threshold share of audio
                        chunks to recognize a user BOT or EOT. Defaults to None.
      :type threshold: float, optional
      :param condition: function that takes an IU
                        and returns a boolean, if True is returned, the
                        speech_counter is incremented. Defaults to None.
      :type condition: Callable[], optional

      :returns: the user BOT or EOT prediction.
      :rtype: boolean



   .. py:method:: recognize()

      Recreates the audio signal received by the microphone by
      concatenating the audio chunks from the audio_buffer and transcribes
      this concatenation into a list of predicted words.

      :returns: the list of transcribed words.
      :rtype: (list[string], boolean)



   .. py:method:: update_current_input()

      Remove from current_input, the oldest IUs, that will not be
      considered to predict user BOT.



   .. py:method:: process_update(update_message)

      Receives and stores VADIUs in the self.current_input buffer.

      :param update_message: UpdateMessage that contains new
                             IUs, if their UpdateType is ADD, they are added to the
                             audio_buffer.
      :type update_message: UpdateType



   .. py:method:: _asr_thread()

      Function that runs on a separate thread.

      Handles the ASR prediction and IUs sending aspect of the module.
      Keeps tracks of the "vad_state" (wheter the user is currently
      speaking or not), and recognizes user BOT or EOT from VADIUs
      received. When "vad_state" == "user_speaking", predicts
      periodically new ASR hypothesis. When user EOT is recognized,
      predicts and sends a final hypothesis.



   .. py:method:: prepare_run()

      Prepare run by instanciating the Thread that transcribes the user
      speech.



   .. py:method:: shutdown()

      Shutdown Thread and Module.



