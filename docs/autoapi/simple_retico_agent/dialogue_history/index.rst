


 


DialogueHistory
===============

.. py:module:: dialogue_history

.. autoapi-nested-parse::

   DialogueHistory
   ===============

   The dialogue history can be used to store every user and agent previous
   turns during a dialogue. You can add data using update its data using
   the append_utterance function, update the current turn stored using
   prepare_dialogue_history and get the updates prompt using get_prompt.

   The DialogueHistory is using a template config file, that you can change
   to configure the prefixes, suffixes, roles, for the user, agent, system
   prompt and the prompt itself. It is useful because every LLm has a
   different prefered template for its prompts.

   Example of a prompt with the following config :
   {
   "user": {
   "role": "Child",
   "role_sep": ":",
   "pre": "",
   "suf": "

   "
   },
   "agent": {
   "role": "Teacher",
   "role_sep": ":",
   "pre": "",
   "suf": "

   "
   },
   "system_prompt": {
   "pre": "<<SYS>>
   ",
   "suf": "<</SYS>>

   "
   },
   "prompt": {
   "pre": "[INST] ",
   "suf": "[/INST]"
   }
   }

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

   simple_retico_agent.dialogue_history.DialogueHistory


Module Contents
---------------

.. py:class:: DialogueHistory(prompt_format_config_file, terminal_logger, file_logger=None, initial_system_prompt='', context_size=2000)

   The dialogue history is where all the sentences from the previvous agent
   and user turns will be stored.

   The LLM, and/or DM will retrieve the history to build the prompt and
   use it to generate the next agent turn.

   Initializes the DialogueHistory.

   :param prompt_format_config_file: path to prompt template
                                     config file.
   :type prompt_format_config_file: str
   :param terminal_logger: The logger used to print
                           events in console.
   :type terminal_logger: TerminalLogger
   :param file_logger: The logger used to store
                       events in a log file.. Defaults to None.
   :type file_logger: FileLogger, optional
   :param initial_system_prompt: The initial system
                                 prompt containing the dialogue scenario and/or
                                 instructions. Defaults to "".
   :type initial_system_prompt: str, optional
   :param context_size: Max number of tokens that the
                        total prompt can contain (LLM context size). Defaults to
                        2000. Defaults to 2000.
   :type context_size: int, optional


   .. py:method:: format_role(config_id)

      Function that format a sentence by adding the role and role
      separation.

      :param config_id: the id to find the corresponding prefix,
                        suffix, etc in the config.
      :type config_id: str

      :returns: the formatted sentence.
      :rtype: str



   .. py:method:: format(config_id, text)

      Basic function to format a text with regards to the
      prompt_format_config. Format meaning to add prefix, sufix, role, etc to
      the text (for agent or user sentence, system prompt, etc).

      :param config_id: the id to find the corresponding prefix,
                        suffix, etc in the config.
      :type config_id: str
      :param text: the text to format with the
                   prompt_format_config.
      :type text: str

      :returns: the formatted text.
      :rtype: str



   .. py:method:: format_sentence(utterance)

      Function that formats utterance, to whether an agent or a user
      sentence.

      :param utterance: a dictionary describing the utterance
                        to format (speaker, and text).
      :type utterance: dict[str]

      :returns: the formatted sentence.
      :rtype: str



   .. py:method:: append_utterance(utterance)

      Add the utterance to the dialogue history.

      :param utterance: a dict containing the speaker and the
                        turn's transcription (text of the sentences).
      :type utterance: dict



   .. py:method:: reset_system_prompt()

      Set the system prompt to initial_system_prompt, which is the prompt
      given at the DialogueHistory initialization.



   .. py:method:: change_system_prompt(system_prompt)

      Function that changes the DialogueHistory current system prompt. The
      system prompt contains the LLM instruction and the scenario of the
      interaction.

      :param system_prompt: the new system_prompt.
      :type system_prompt: str

      :returns: the previous system_prompt.
      :rtype: str



   .. py:method:: prepare_dialogue_history(fun_tokenize)

      Calculate if the current dialogue history is bigger than the LLM's
      context size (in nb of token). If the dialogue history contains too
      many tokens, remove the older dialogue turns until its size is smaller
      than the context size. The self.cpt_0 class argument is used to store
      the id of the older turn of last prepare_dialogue_history call (to
      start back the while loop at this id).

      :param fun_tokenize: the tokenize function given by
                           the LLM, so that the DialogueHistory can calculate the
                           right dialogue_history size.
      :type fun_tokenize: Callable[]

      :returns:

                the prompt to give to the LLM (containing the
                    formatted system prompt, and a maximum of formatted
                    previous sentences), and it's size in nb of token.
      :rtype: (text, int)



   .. py:method:: interruption_alignment_new_agent_sentence(utterance, punctuation_ids, interrupted_speaker_iu)

      After an interruption, this function will align the sentence stored
      in dialogue history with the last word spoken by the agent. With the
      informations stored in interrupted_speaker_iu, this function will
      shorten the utterance to be aligned with the last words spoken by the
      agent.

      :param utterance: the utterance generated by the LLM,
                        that has been interrupted by the user and needs to be
                        aligned.
      :type utterance: dict[str]
      :param punctuation_ids: the id of the punctuation
                              marks, calculated by the LLM at initialization.
      :type punctuation_ids: list[int]
      :param interrupted_speaker_iu: the
                                     SpeakerModule's IncrementalUnit, used to align the agent
                                     utterance.
      :type interrupted_speaker_iu: IncrementalUnit



   .. py:method:: get_dialogue_history()

      Get DialogueHistory's dictionary containing the system prompt and
      all previous turns.

      :returns: DialogueHistory's dictionary.
      :rtype: dict



   .. py:method:: get_prompt(start=1, end=None, system_prompt=None)

      Get the formatted prompt containing all turns between start and end.

      :param start: start id of the oldest turn to take.
                    Defaults to 1.
      :type start: int, optional
      :param end: end id of the latest turn to take.
                  Defaults to None.
      :type end: int, optional

      :returns: the corresponding formatted prompt.
      :rtype: str



   .. py:method:: get_stop_patterns()

      Get stop patterns for both user and agent.

      :returns: user and agent stop patterns.
      :rtype: tuple[bytes], tuple[bytes]



