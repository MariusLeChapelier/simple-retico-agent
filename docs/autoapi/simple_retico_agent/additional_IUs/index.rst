


 


Additional IUs
==============

.. py:module:: additional_IUs

.. autoapi-nested-parse::

   Additional IUs
   ==============

   Additional Incremental Unit classes used in Simple Retico Agent.




Classes
-------

.. autoapisummary::

   simple_retico_agent.additional_IUs.TextFinalIU
   simple_retico_agent.additional_IUs.AudioFinalIU
   simple_retico_agent.additional_IUs.VADIU


Module Contents
---------------

.. py:class:: TextFinalIU(final=False, **kwargs)

   Bases: :py:obj:`retico_core.text.TextIU`


   TextIU with an additional final attribute.

   Initialize an abstract IU. Takes the module that created the IU as an
   argument.

   :param creator: The module that created this incremental
                   unit.
   :type creator: AbstractModule
   :param iuid: The id of the IU. This should be a unique ID given by the module
                that produces the incremental unit and is used to identify the IU later
                on - for example when revoking an IU.
   :type iuid: int
   :param previous_iu: A link to the incremental unit
                       created before the current one by the same module.
   :type previous_iu: IncrementalUnit
   :param grounded_in: A link to the incremental unit that
                       this one is based on.
   :type grounded_in: IncrementalUnit
   :param payload: A generic payload that can be set.


   .. py:method:: type()
      :staticmethod:


      Return the type of the IU in a human-readable format.

      :returns: The type of the IU in a human-readable format.
      :rtype: str



.. py:class:: AudioFinalIU(final=False, **kwargs)

   Bases: :py:obj:`retico_core.audio.AudioIU`


   AudioIU with an additional final attribute.

   Initialize an abstract IU. Takes the module that created the IU as an
   argument.

   :param creator: The module that created this incremental
                   unit.
   :type creator: AbstractModule
   :param iuid: The id of the IU. This should be a unique ID given by the module
                that produces the incremental unit and is used to identify the IU later
                on - for example when revoking an IU.
   :type iuid: int
   :param previous_iu: A link to the incremental unit
                       created before the current one by the same module.
   :type previous_iu: IncrementalUnit
   :param grounded_in: A link to the incremental unit that
                       this one is based on.
   :type grounded_in: IncrementalUnit
   :param payload: A generic payload that can be set.


   .. py:method:: type()
      :staticmethod:


      Return the type of the IU in a human-readable format.

      :returns: The type of the IU in a human-readable format.
      :rtype: str



.. py:class:: VADIU(va_user=None, va_agent=None, **kwargs)

   Bases: :py:obj:`retico_core.audio.AudioIU`


   AudioIU enhanced by VADModule with VA for both user and agent.

   .. attribute:: va_user

      user VA activation, True means voice recognized,
      False means no voice recognized.

      :type: bool

   .. attribute:: va_agent

      agent VA activation, True means audio outputted
      by the agent, False means no audio outputted by the agent.

      :type: bool

   Initialize an abstract IU. Takes the module that created the IU as an
   argument.

   :param creator: The module that created this incremental
                   unit.
   :type creator: AbstractModule
   :param iuid: The id of the IU. This should be a unique ID given by the module
                that produces the incremental unit and is used to identify the IU later
                on - for example when revoking an IU.
   :type iuid: int
   :param previous_iu: A link to the incremental unit
                       created before the current one by the same module.
   :type previous_iu: IncrementalUnit
   :param grounded_in: A link to the incremental unit that
                       this one is based on.
   :type grounded_in: IncrementalUnit
   :param payload: A generic payload that can be set.


   .. py:method:: type()
      :staticmethod:


      Return the type of the IU in a human-readable format.

      :returns: The type of the IU in a human-readable format.
      :rtype: str



