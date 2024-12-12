


 


SimpleLLMModule
===============

.. py:module:: simple_llm

.. autoapi-nested-parse::

   SimpleLLMModule
   ===============

   A retico module that provides Natural Language Generation (NLG) using a
   Large Language Model (LLM).

   When a full user sentence (COMMIT SpeechRecognitionIUs) is received from
   the ASR (a LLM needs a complete sentence to compute Attention), the
   module adds the sentence to the previous dialogue turns stored in the
   dialogue history, builds the prompt using the previous turns (and
   following a defined template), then uses the prompt to generates a
   system answer. IUs are created from the generated words, and are sent
   incrementally during the genration. Each new word is ADDED, and if if a
   punctuation is encountered (end of clause), the IUs corresponding to the
   generated clause are COMMITED. The module records the dialogue history
   by saving the dialogue turns from both the user and the agent, it gives
   the context of the dialogue to the LLM, which is very important to
   maintain a consistent dialogue. Update the dialogue history so that it
   doesn't exceed a certain threshold of token size. Put the maximum number
   of previous turns in the prompt at each new system sentence generation.

   The llama-cpp-python library is used to improve the LLM inference speed
   (execution in C++).

   Inputs : SpeechRecognitionIU, VADTurnAudioIU, TextAlignedAudioIU

   Outputs : TurnTextIU

   Example of default prompt template:
   prompt = "[INST] <<SYS>>
   This is a spoken dialog scenario between a teacher and a 8 years old
   child student. The teacher is teaching mathematics to the child student.
   As the student is a child, the teacher needs to stay gentle all the
   time. Please provide the next valid response for the following
   conversation. You play the role of a teacher. Here is the beginning of
   the conversation :
   <</SYS>>

   Child : Hello !

   Teacher : Hi! How are you today ?

   Child : I am fine, and I can't wait to learn mathematics!

   [/INST]
   Teacher :"




Classes
-------

.. autoapisummary::

   simple_retico_agent.simple_llm.SimpleLLMModule


Module Contents
---------------

.. py:class:: SimpleLLMModule(model_path, model_repo, model_name, dialogue_history: simple_retico_agent.dialogue_history.DialogueHistory, device=None, context_size=2000, n_gpu_layers=100, top_k=40, top_p=0.95, temp=1.0, repeat_penalty=1.1, verbose=False, **kwargs)

   Bases: :py:obj:`retico_core.AbstractModule`


   A retico module that provides Natural Language Generation (NLG) using a
   Large Language Model (LLM).

   When a full user sentence (COMMIT SpeechRecognitionIUs) is received
   from the ASR (a LLM needs a complete sentence to compute Attention),
   the module adds the sentence to the previous dialogue turns stored
   in the dialogue history, builds the prompt using the previous turns
   (and following a defined template), then uses the prompt to
   generates a system answer. IUs are created from the generated words,
   and are sent incrementally during the genration. Each new word is
   ADDED, and if if a punctuation is encountered (end of clause), the
   IUs corresponding to the generated clause are COMMITED. The module
   records the dialogue history by saving the dialogue turns from both
   the user and the agent, it gives the context of the dialogue to the
   LLM, which is very important to maintain a consistent dialogue.
   Update the dialogue history so that it doesn't exceed a certain
   threshold of token size. Put the maximum number of previous turns in
   the prompt at each new system sentence generation.

   The llama-cpp-python library is used to improve the LLM inference
   speed (execution in C++).

   Inputs : SpeechRecognitionIU, VADTurnAudioIU, TextAlignedAudioIU

   Outputs : TurnTextIU

   Initializes the SimpleLLMModule Module.

   :param model_path: local model instantiation. The path to
                      the desired local model weights file
                      (my_models/mistral-7b-instruct-v0.2.Q4_K_M.gguf for
                      example).
   :type model_path: string
   :param model_repo: HF model instantiation. The path to the
                      desired remote hugging face model
                      (TheBloke/Mistral-7B-Instruct-v0.2-GGUF for example).
   :type model_repo: string
   :param model_name: HF model instantiation. The name of the
                      desired remote hugging face model
                      (mistral-7b-instruct-v0.2.Q4_K_M.gguf for example).
   :type model_name: string
   :param dialogue_history: The initialized
                            DialogueHistory that will contain the previous user and
                            agent turn during the dialogue.
   :type dialogue_history: DialogueHistory
   :param device: the device the module will run on
                  (cuda for gpu, or cpu)
   :type device: string, optional
   :param context_size: Max number of tokens that the
                        total prompt can contain. Defaults to 2000.
   :type context_size: int, optional
   :param n_gpu_layers: Number of model layers you
                        want to run on GPU. Take the model nb layers if greater.
                        Defaults to 100.
   :type n_gpu_layers: int, optional
   :param top_k: LLM generation parameter. Defaults to
                 40.
   :type top_k: int, optional
   :param top_p: LLM generation parameter. Defaults
                 to 0.95.
   :type top_p: float, optional
   :param temp: LLM generation parameter. Defaults
                to 1.0.
   :type temp: float, optional
   :param repeat_penalty: LLM generation parameter.
                          Defaults to 1.1.
   :type repeat_penalty: float, optional
   :param verbose: LLM verbose. Defaults to False.
   :type verbose: bool, optional


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



   .. py:method:: init_stop_criteria()

      Calculates the stopping token patterns using the instantiated model
      tokenizer.



   .. py:method:: new_user_sentence(user_sentence)

      Function called to register a new user sentence into the dialogue
      history (utterances attribute). Calculates the exact token number added
      to the dialogue history (with template prefixes and suffixes).

      :param user_sentence: the new user sentence to register.
      :type user_sentence: string



   .. py:method:: new_agent_sentence(agent_sentence)

      Function called to register a new agent sentence into the dialogue
      history (utterances attribute). Calculates the exact token number added
      to the dialogue history (with template prefixes and suffixes).

      :param agent_sentence: the new agent sentence to register.
      :type agent_sentence: string
      :param agent_sentence_nb_tokens: the number of token
                                       corresponding to the agent sentence (without template
                                       prefixes and suffixes).
      :type agent_sentence_nb_tokens: int



   .. py:method:: remove_stop_patterns(sentence, pattern_id)

      Function called when a stopping token pattern has been encountered
      during the sentence generation. Remove the encountered pattern from the
      generated sentence.

      :param sentence: Agent new generated sentence containing a
                       stopping token pattern.
      :type sentence: string

      :returns:

                Agent new generated sentence without the stopping
                    token pattern encountered. int: nb tokens removed (from
                    the stopping token pattern).
      :rtype: bytes



   .. py:method:: identify_and_remove_stop_patterns(sentence)

      Function called when a stopping token pattern has been encountered
      during the sentence generation. Remove the encountered pattern from the
      generated sentence.

      :param sentence: Agent new generated sentence containing a
                       stopping token pattern.
      :type sentence: string

      :returns:

                Agent new generated sentence without the stopping
                    token pattern encountered. int: nb tokens removed (from
                    the stopping token pattern).
      :rtype: string



   .. py:method:: remove_role_patterns(sentence)

      Function called when a role token pattern has been encountered
      during the sentence generation. Remove the encountered pattern from the
      generated sentence.

      :param sentence: Agent new generated sentence containing a
                       role token pattern.
      :type sentence: string

      :returns:

                the agent new generated sentence without the
                    role token pattern, and the number of token removed
                    while removing the role token pattern from the sentence.
      :rtype: (bytes, int)



   .. py:method:: prepare_dialogue_history()

      Calculate if the current dialogue history is bigger than the size
      threshold (short_memory_context_size).

      If the dialogue history contains too many tokens, remove the
      oldest dialogue turns until its size is smaller than the
      threshold.



   .. py:method:: is_punctuation(word)

      Returns True if the token correspond to a punctuation.

      :param word: a detokenized word corresponding to last
                   generated LLM token
      :type word: bytes

      :returns: True if the token correspond to a punctuation.
      :rtype: bool



   .. py:method:: is_stop_token(token)

      Function used by the LLM to stop generate tokens when it meets
      certain criteria.

      :param token: last token generated by the LLM
      :type token: int
      :param word: the detokenized word corresponding to last
                   generated token
      :type word: bytes

      :returns:

                returns True if it the last generated token
                    corresponds to self.stop_token_ids or
                    self.stop_token_text.
      :rtype: bool



   .. py:method:: is_stop_pattern(sentence)

      Returns True if one of the stopping token patterns matches the end
      of the sentence.

      :param sentence: a sentence.
      :type sentence: string

      :returns:

                True if one of the stopping token patterns matches the
                    end of the sentence.
      :rtype: bool



   .. py:method:: is_role_pattern(sentence)

      Returns True if one of the role token patterns matches the beginning
      of the sentence.

      :param sentence: a sentence.
      :type sentence: string

      :returns:

                True if one of the role token patterns matches the
                    beginning of the sentence.
      :rtype: bool



   .. py:method:: generate_next_sentence(prompt_tokens)

      Generates the agent next sentence from the constructed prompt
      (dialogue scenario, dialogue history, instruct...). At each generated
      token, check is the end of the sentence corresponds to a stopping
      pattern, role pattern, or punctuation. Sends the info to the retico
      Module using the submodule function. Stops the generation if a stopping
      token pattern is encountered (using the
      stop_multiple_utterances_generation as the stopping criteria).

      :param subprocess: the function to call during the
                         sentence generation to possibly send chunks of sentence
                         to the children modules.
      :type subprocess: function
      :param top_k: _description_. Defaults to 40.
      :type top_k: int, optional
      :param top_p: _description_. Defaults to 0.95.
      :type top_p: float, optional
      :param temp: _description_. Defaults to 1.0.
      :type temp: float, optional
      :param repeat_penalty: _description_. Defaults to
                             1.1.
      :type repeat_penalty: float, optional

      :returns:

                agent new generated sentence. int: nb tokens in new
                    agent sentence.
      :rtype: bytes



   .. py:method:: recreate_sentence_from_um(msg)

      Recreate the complete user sentence from the strings contained in
      every COMMIT update message IU (msg).

      :param msg: list of every COMMIT IUs contained in the
                  UpdateMessage.
      :type msg: list

      :returns: the complete user sentence calculated by the ASR.
      :rtype: string



   .. py:method:: incremental_iu_sending(payload, is_punctuation=None, role_pattern=None)

      This function will be called by the submodule at each token
      generation. It handles the communication with the subscribed module
      (TTS for example), by updating and publishing new UpdateMessage
      containing the new IUS.

      IUs are : ADDED in every situation (the generated words are sent
      to the subscribed modules). COMMITTED if the last token
      generated is a punctuation (The TTS can start generating the
      voice corresponding to the clause). REVOKED if the last tokens
      generated corresponds to a role pattern (so that the subscribed
      module delete the role pattern)

      :param payload: the text corresponding to the last
                      generated token
      :type payload: string
      :param is_punctuation: True if the last generated
                             token correspond to a punctuation. Defaults to None.
      :type is_punctuation: bool, optional
      :param stop_pattern: Text corresponding to the
                           generated stop_pattern. Defaults to None.
      :type stop_pattern: string, optional



   .. py:method:: process_incremental()

      Core function of the module, it recreates the user sentence, adds it
      to dialogue history, gets the updated prompt, generates the agent next
      sentence (internal calls will incrementally send IUs during the
      generation), COMMITS the new agent sentence once the generation is
      over, and finally adds the sentence to the dialogue history.



   .. py:method:: process_update(update_message)

      Process new SpeechRecognitionIUs received, if their UpdateType is
      COMMIT (complete user sentence).

      :param update_message: UpdateMessage that contains
                             new IUs, if their UpdateType is COMMIT, they correspond
                             to a complete sentence. The complete sentence is
                             processed calling the process_incremental function.
      :type update_message: UpdateMessage



   .. py:method:: _llm_thread()

      Function running the LLM, executed in a separated thread so that the
      LLM can still receive messages during generation.



   .. py:method:: setup(**kwargs)

      Instantiate the model with the given model info, if insufficient
      info given, raise an NotImplementedError.

      Calculates stopping criteria (tokens, patterns, roles, etc) with
      the init_stop_criteria function.



   .. py:method:: prepare_run()

      Prepare module execution by instanciating the generation Thread.



   .. py:method:: shutdown()

      This method is called before the module is stopped. This method can
      be used to tear down the pipeline needed for processing the IUs.



