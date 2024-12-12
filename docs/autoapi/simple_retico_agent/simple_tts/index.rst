


 


SimpleTTSModule
===============

.. py:module:: simple_tts

.. autoapi-nested-parse::

   SimpleTTSModule
   ===============

   A retico module that provides Text-To-Speech (TTS) to a retico system by
   transforming TextFinalIUs into AudioFinalIUs, clause by clause. When
   receiving COMMIT TextFinalIU from the LLM, i.e. TextFinalIUs that
   consists in a full clause. Synthesizes audio (AudioFinalIUs)
   corresponding to all IUs contained in UpdateMessage (the complete
   clause). The module only sends TextFinalIU with a fixed raw_audio
   length.

   This modules uses the deep learning approach implemented with coqui-ai's
   TTS library : https://github.com/coqui-ai/TTS

   Inputs : TextFinalIU

   Outputs : AudioFinalIU




Classes
-------

.. autoapisummary::

   simple_retico_agent.simple_tts.SimpleTTSModule


Module Contents
---------------

.. py:class:: SimpleTTSModule(model='jenny', language='en', speaker_wav='TTS/wav_files/tts_api/tts_models_en_jenny_jenny/long_2.wav', frame_duration=0.2, verbose=False, device=None, **kwargs)

   Bases: :py:obj:`retico_core.AbstractModule`


   A retico module that provides Text-To-Speech (TTS) to a retico system by
   transforming TextFinalIUs into AudioFinalIUs, clause by clause. When
   receiving COMMIT TextFinalIU from the LLM, i.e. TextFinalIUs that consists
   in a full clause. Synthesizes audio (AudioFinalIUs) corresponding to all
   IUs contained in UpdateMessage (the complete clause). The module only sends
   TextFinalIU with a fixed raw_audio length.

   This modules uses the deep learning approach implemented with coqui-
   ai's TTS library : https://github.com/coqui-ai/TTS

   Inputs : TextFinalIU

   Outputs : AudioFinalIU

   Initializes the SimpleTTSModule.

   :param model: name of the desired model, has to be
                 contained in the constant LANGUAGE_MAPPING.
   :type model: string
   :param language: language of the desired model, has to be
                    contained in the constant LANGUAGE_MAPPING.
   :type language: string
   :param speaker_wav: path to a wav file containing the
                       desired voice to copy (for voice cloning models).
   :type speaker_wav: string
   :param frame_duration: duration of the audio chunks
                          contained in the outputted AudioFinalIUs.
   :type frame_duration: float
   :param verbose: the verbose level of the TTS
                   model. Defaults to False.
   :type verbose: bool, optional
   :param device: the device the module will run on
                  (cuda for gpu, or cpu)
   :type device: string, optional


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



   .. py:method:: synthesize(text)

      Takes the given text and synthesizes speech using the TTS model.
      Returns the synthesized speech as 22050 Hz int16-encoded numpy ndarray.

      :param text: The text to use to synthesize speech.
      :type text: str

      :returns: The speech as a 22050 Hz int16-encoded numpy ndarray.
      :rtype: bytes



   .. py:method:: one_clause_text_and_words(clause_ius)

      Convert received IUs data accumulated in current_input list into a
      string.

      :returns: sentence chunk to synthesize speech from.
      :rtype: string



   .. py:method:: process_update(update_message)

      Process the COMMIT TextFinalIUs received by appending to
      self.current_input the list of IUs corresponding to the full clause.



   .. py:method:: get_new_iu_buffer_from_clause_ius(clause_ius)

      Function that take all TextFinalIUs from one clause, synthesizes the
      corresponding speech and split the audio into AudioFinalIUs of a fixed
      raw_audio length.

      :returns:

                the generated AudioFinalIUs, with a
                    fixed raw_audio length, that will be sent to the speaker
                    module.
      :rtype: list[AudioFinalIU]



   .. py:method:: setup()

      Setup Module by instanciating the TTS model and its related audio
      attributes.



   .. py:method:: prepare_run()

      Prepare run by instanciating the Thread that synthesizes the
      audio.



   .. py:method:: shutdown()

      Shutdown Thread and Module.



