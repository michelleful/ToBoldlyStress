ToBoldlyStress
==============

Bold stressed syllables in arbitrary English text.

Background
----------

Based on a suggestion by Reddit user /u/enthusiastOfRustMayb
([link](http://www.reddit.com/r/language/comments/2bdpeu/teaching_french_spoken_english_emphasis_on/)),
help English learners, especially those of a language without word stress or with different stress cues,
to identify which syllable to stress. This is done by bolding stressed syllables in their orthographic form
(a bit tricky as most stress information comes in phonetic form).


Usage
-----
The main function is *process_text* in *stress.py*

process_text("Hello world! Look who's talking!")
> "He<b>llo</b> <b>world</b>! <b>Look</b> <b>who's</b> <b>tal</b>king!"

Acknowledgments
---------------

I have made use of the following prior work:
- [The CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict)
- [The syllabified version of CMUDICT, produced by Joshua Tauberer (UPenn)](http://www.ling.upenn.edu/phonetics/p2tk/)
- [m2m-aligner by Sittichai Jiampojamarn (University of Alberta)](http://code.google.com/p/m2m-aligner/)


Contact
-------
Written by Michelle Fullwood (michelle.fullwood@gmail.com)
