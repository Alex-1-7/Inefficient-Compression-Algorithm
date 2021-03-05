# Inefficient-Compression-Algorithm
Challenge for a job application


Challenge:

Searchlight Inefficient Compression Scheme
==========================================

Write a compression and decompression algorithm for SICS which works as follows:

Find the most popular characters, and in order of popularity assign them a hex value 0 to E, F0 to FE, FF0 to FFE, etc.  Note, an F indicates that there are more nibbles to follow, anything else is the terminal nibble.  Compress the message by replacing characters with their assigned value.

Test case:

text = "Marley was dead: to begin with. There is no doubt whatever about that. The register of his burial was signed by the clergyman, the clerk, the undertaker, and the chief mourner. Scrooge signed it: and Scrooge’s name was good upon ’Change, for anything he chose to put his hand to. Old Marley was as dead as a door-nail. Mind! I don’t mean to say that I know, of my own knowledge, what there is particularly dead about a door-nail. I might have been inclined, myself, to regard a coffin-nail as the deadest piece of ironmongery in the trade. But the wisdom of our ancestors is in the simile; and my unhallowed hands shall not disturb it, or the Country’s done for. You will therefore permit me to repeat, emphatically, that Marley was as dead as a door-nail."

solution = "f826b1d0e2a08128fd0340f61f0750e739f50fe916107a054084cf630e9231ff01602f64c303923f50fe91061f07a31604f3097a0f6c672b0e2a0a7f05180f6d03910f2b16f0df125f403910f2b16f9f403910c581632f916f4025803910f2971f30f14c6516f50ff1f2644f010a7f0518073fd02580ff1f2644f01faa052f110e2a0f04480cf7450faff2925f01f40f346025d3975f00910f294a10340f7c3097a09258034f50ff3b80f826b1d0e2a02a0812802a0208446fb527bf50f8758ff40fc0845fa30f11250340a2d039230fc0f954ef404f30f1d04e50f954eb18f01f40e92303916107a0f72637f2cb26bd0812802f64c30208446fb527bf50fc0f17f093092ff010f6115075f2b7518f40f1da1bf3f4034061f0268020f24f3f375fb527b02a0391081281a30f771f2104f307645f145f016d0750391036281f50ff5c303910e7a84f104f304c6025f21a346a07a07503910a7f17b1ff602580f1d0c592bb4e1809258a0a92bb0543087a3c6f6073f404603910ff24c536dfaa084510f346f50ff74c0e7bb039161f34610f716f1730f11034061f7123f401f1f79237f22bbdf4039230f826b1d0e2a02a0812802a0208446fb527bf5"

