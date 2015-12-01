c     SURVEY PROGRAM...........sur2012.f
c
c     Computers do what you say, not what you mean.
c
c     YOU M U S T FOLLOW INSTRUCTIONS and submit as written
c     below to get full points. ``PRINT'' the file, email
c     the datafile exactly as explained.
c
c     This is a fortran program and also Targil 1 of the course.
c     all class targilim graded out of 10, including this one.
c     you may request help before the due date, (for this targil Dr Adler
c     will give as much help as needed before the due date) B U T  delays 
c     in handing in cost 2 points first day; 4 points 2nd day etc.
c
c     This program will survey your computer experience
c     to help me set class level and arrange extra help if needed.
c     (anyone who wishes to translate this program to c may do so and
c     will receive extra credit (4 points), but you must also run the
c     fortran one because it teaches skills you need in the course.) 
c     A good computational physicist may write in any of several languages
c     but must read many more. This program is intentionally written in
c     in an old-fashioned fortran to show you how to handle format statements
c     that you will find in older codes.  It is also meant to check that you
c     have mastered all the printing and emailing skills you will need
c     later in the course. So ASK if you need help with these.
c
c     In this course PRINTING means either printing on paper or
c     handing in a piece of paper with the location
c     of the file on a web page where Dr Adler can access it,
c     (on physics, t2 or tx). You decide each time how you want to
c     ``PRINT''. Sending an email is not the same as printing.
c     Sometimes I ask you to email programs or data files, but usually 
c     you should ``PRINT'' targilim.
c
c     YOU MUST HAND IN THE PRINTED VERSION WITH THE SPACES FILLED
c     EITHER ON PAPER or WRITE THE WEB LOCATION ON PAPER.
c 
c     YOU ALSO HAVE TO COMPILE AND RUN THE PROGRAM 
c     AND THEN  EMAIL ME THE OUTPUT FILE  FOR FULL CREDIT!
c     see http://phycomp.technion.ac.il/~comphy/commands.html
c     if you do not know how to email files or download files
c     from the web, or run a fortran program, 
c     now is your chance to learn these!
c     This is the ONLY time I accept homework via email.
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c     Now about this program:
c     the first thing to know is that a line beginning with c  is a comment
c     you can write anything on a comment line. The compiler ignores these
c     take care when modifying lines that do not start with c !!
c     the lines that do not start with c   are the real program
c
c     INFORMATION FOR DR ADLER.............................................
c     please fill in your name:
c                             ..Emma Schmidgall…………………
c                         faculty: 
c                             …Physics………………..
c                         degree:          room:     tel. no:
c                                 ….P…hD..    …SSI… 100        .0523118069..
c                         areas of interest in physics:
c                                                     ..quantum information….
c
c                                                     ..solid state physics..
c     I have an idea for the final project  
c     in the area of:                  ....................................
c     I have no specific idea but would
c     like a project in the area of:   ....................................
c     I have no idea and would like suggestions:
c                                      ….I …guess I’m more here……….
c          
c     INSTRUCTIONS....................................................
c     Please indicate your knowledge of different computers/languages/
c     operating systems etc by changing the values 10000.0 to either 1.0 or 0.0
c     set the quantities equal to 1.0 if you have some idea of the computer/
c     operating system/language etc.
c     Set the quantities equal to 0.0 if you dont know what they are or
c     anything at all about their use.
c     For example..if you could have written a simple fortran program like
c     this one your knowledge of fortran is sufficient to set fortran=1.0.
c     Please reset each quantity on this survey.
c
c     Please hand in a printed version of this survey with
c     your name and data to Dr. Adler either to her letterbox, 4th floor 
c     LIDOW physics building by 18:00 on the day of the lecture in three weeks.
c     Please also return the data file that this program generates
c     by electronic mail to phr76ja@tx.technion.ac.il
c     before 18:00 on the day of the   lecture in three weeks.
c     Please write your preferred electronic mail address
c     on a Technion machine - no yahoo, gmail etc
c     e-mail address:
c                   ...................................
c     if this address is not on t2(undergraduates) or tx(graduates)
c     please open an account on one of those. (new students see Riva for this).
c     as well as the above you must also have an account on PHELAFEL/PHCLASS
c     which will be opened after you have filled out the form for this
c     and opened your account on tx or t2. for the purposes of this program
c     your account name on PHELAFEL will be called YOURIDX. please 
c     write it here:
c                  .....................
c
c     You may not know what all the items below mean, so just answer 0.0
c     to any you do not understand.
c
c     TECHNICAL NOTE..................................................
c     some quantities whose names begin with the letters i,j,k,l,m, or  n
c     need to be set to be real variables in a fortran program.
      real manual,mainf,java,LINUX
c
c     PREVIOUS ACCESS TO COMPUTERS....................................
c     used computers at school
      cs=1.0
c     taken programming course at university
      prog=0.0
c     have a home computer/laptop
      home=1.0
c     taken a course with targilim on a computer in physics/chemistry etc
      course=1.0
c     have a computer in your office/lab
      offlab=1.0
c
c     LANGUAGES.......................................................
      fortran=0.0
      pascal=0.0
      basic=1.0
c     c/c++    
      c=1.0
      algol=1.0
      pl1=0.0
      java=0.0
      html=1.0
      python=1.0
c
c     OPERATING SYSTEMS..............................................
c     unix or linux
      unix=1.0
      windows=1.0

c
c     EDITORS........................................................
c     a unix editor
      vi=0.0
      emacs=1.0
      unikedit=0.0
c
c     MAINFRAME COMPUTERS...........................................
c     any mainframe
      mainf=0.0
c     write the name here:
c                                               ...................
c     previous experience with a supercomputer:
c                                             .....................
      super=0.0
c     previous experience with a parallel machine:
c                                             .....................
      par=0.0
c
c     LINUX computer.................................................
      linux=1.0
c     other unix:
c          ........................
c

c     YOUR CURRENT ACCESS TO COMPUTERS.............................
c     personal computer at home, friends, lab  etc to which you have
c     free access and would LIKE to do some targilim or projects
c     from this course.
c     (this is not neccessary! you will have adequate access to the
c     phclassess and PHELAFEL  for all course work, it is just to help
c     me allocate resources.)
c     type of computer:
c                     ……..Mac………………………………
c     operating system:
c                     ….OSX Yosemite 10.10.4…………..
c     languages:
c                     …Python, Matlab, C…………
c                     ............................................
c     I have no independent access to computers and would like to
c     do all course work on physics department computers:
c                                                    ….No……
c     (this will be organised for whoever needs it)
c
c     TIKSHORET...................................................
c     previous experience with unix email (e.g.pine, webmail)
      uemail=1.0
c     previous experience with other electronic mail (e.g. eudora)
      email=1.0
c     previous experience with telnet/ftp/ssh/scp
      telnet=1.0
c     previous experience with internet/web writing
      web=1.0
c
c     YEUTZ......................................................
c     I have read a computer hardware/software manual
      manual=1.0
c     I have used a help file
      help=1.0
c
c     WORD PROCESSORS...........................................
c     previous experience with tex/latex
      tex=1.0
c     previous experience with word
      word=1.0
c                                 ..............................
c
c     SOFTWARE PACKAGES.........................................
c     please list software packages (mathematica, matlab etc)
c     that you have used:
c                        …Matlab, Mathematica, Maple, LabView
c
c
c     DATA ANALYSIS.............................................
c     the remainder of this program organises your replies for
c     transmission to Dr. Adler.
c     it prepares a file that will be read by the analysis  routine.
c     if you are new to fortran
c     as a simple fortran exercise try to write your own analysis routine.
c     you may also try to write an analysis routine in c.
c     bonus points will be given for either.
c     please print this file before emailing to Dr. Adler to check
c     that  you have set all quantities  to 1.0 or to 0.0
c     you will lose points if you fail to reset all quantities.
c     PRINTING onto dataset youridx.out...........................
c     remember to change youridx to your id
      open (unit=6,file='youridx.out',status='new')
      write (6,100)cs,prog,home,course,offlab
      write (6,200)fortran,pascal,basic,c,algol,pl1,python
      write (6,250)java,html
      write (6,300)unix,windows
      write (6,400)vi,emacs,unikedit
      write (6,500)mainf,super,par     
      write (6,550)linux
      write (6,700)uemail,email,telnet,web
      write (6,800)manual,help
      write (6,900)tex,word
      num=0
      write (6,80)num
      write (6,101)cs,prog,home,course,offlab
      write (6,201)fortran,pascal,basic
      write (6,202)c,algol,pl1,python
      write (6,252)java,html 
      write (6,301)unix,windows
      write (6,402)vi,emacs,unikedit
      write (6,501)mainf
      write (6,503)super,par
      write (6,552)linux
      write (6,701)uemail,email
      write (6,702)telnet,web
      write (6,801)manual,help
      write (6,901)tex,word
      
   80 format (i5)
  100 format (5f8.1)
  200 format (7f8.1)
  250 format (2f8.1)
  300 format (2f8.1)
  400 format (3f8.1)
  500 format (3f8.1)
  550 format (1f8.1)
  600 format (6f8.1)
  700 format (4f8.1)
  800 format (2f8.1)
  900 format (2f8.1)
  101 format(' cs=  ',f8.1,' prog=  ',f8.1,' home=  ',f8.1,
     x 'course=  ',f8.1,'offlab=  ',f8.1)
  201 format(' fortran=  ',f8.1,' pascal=  ',f8.1,' basic=  ',f8.1)
  202 format(' c=  ',f8.1,' algol=  ',f8.1,' pl1=  ',f8.1,
     x ' python=  ',f8.1)
  252 format('  java=',f8.1,' html=', f8.1 )
  301 format(' unix=  ',f8.1,' windows=  ',f8.1)
  402 format(' vi=    ',f8.1,' emacs=   ',f8.1,'  unikedit=  ',f8.1)
  501 format(' mainf= ',f8.1)
  503 format(' super=  ',f8.1,' par=  ',f8.1)
 
  552 format(' linux=',f8.1)
  701 format(' uemail=  ',f8.1,' email=  ',f8.1)
  702 format(' telnet=  ',f8.1,' web=  ',f8.1)
  801 format(' manual=  ',f8.1,' help=  ',f8.1)
  901 format(' tex=  ',f8.1,' word=  ',f8.1)
  

      stop
      end

