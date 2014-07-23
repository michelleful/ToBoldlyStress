ToBoldlyStress
==============

Bold stressed syllables in arbitrary English text.

Background
----------

Based on a suggestion by Reddit user /u/enthusiastOfRustMayb
([link](http://www.reddit.com/r/language/comments/2bdpeu/teaching_french_spoken_english_emphasis_on/)),
help English learners, especially those speakers of a language without word stress or with different stress cues,
to identify which syllable to stress. This is done by bolding stressed syllables in their orthographic form
(a bit tricky as most stress information comes in phonetic form).

Now available online at [http://stressifier.herokuapp.com](http://stressifier.herokuapp.com)

Usage
-----
The main function is *process_text* in *stress.py*

process_text("Hello world! Look who's talking!")
> "He<b>llo</b> <b>world</b>! <b>Look</b> <b>who's</b> <b>tal</b>king!"

(Note: in the online app, single syllables are unbolded for less visual clutter.)

Acknowledgments
---------------

I have made use of the following prior work:
- [The CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict)
- [The syllabified version of CMUDICT, produced by Joshua Tauberer (UPenn)](http://www.ling.upenn.edu/phonetics/p2tk/)
- [m2m-aligner by Sittichai Jiampojamarn (University of Alberta)](http://code.google.com/p/m2m-aligner/)

Citation: Sittichai Jiampojamarn, Grzegorz Kondrak and Tarek Sherif (2007). Applying Many-to-Many Alignments and Hidden Markov Models to Letter-to-Phoneme Conversion. HLT 2007 (ACL), 372-379. http://www.aclweb.org/anthology/N/N07/N07-1047.



Contact
-------
Written by Michelle Fullwood (michelle.fullwood@gmail.com)
