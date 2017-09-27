#!/usr/bin/env python

import os                               # Operating system
import time                             # Time functions
import sys                              # System functions
import glob                             # Filename globbing
import re                               # Regular expressions
import csv
import string
import random
import json
import Commands
import shutil

from PIL import Image

flgNonModal = True


imSuffixes = ( '*.jpg', '*.JPG',
               '*.jpeg', '*.JPEG',
               '*.png', '*.PNG',
               '*.tif', '*.TIF',
               '*.tiff', '*.TIFF' )



# Open the menu sidebar html file
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

foutMenu = open( 'menu.html', 'wb')

foutMenu.write( '<!DOCTYPE html>\n\n' )
foutMenu.write( '<html>\n' )
foutMenu.write( '  <head>\n' )
foutMenu.write( '    <link rel="stylesheet" type="text/css" href="style.css">\n' )
foutMenu.write( '    <title>SidebarPage</title>\n' )
foutMenu.write( '  </head>\n\n' )
foutMenu.write( '  <body>\n\n' )
foutMenu.write( '    <ul style="list-style-type:none">\n\n' )


# Open the main html file
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

foutMain = open( 'main.html', 'wb')

foutMain.write( '<!DOCTYPE html>\n\n' )
foutMain.write( '<html>\n' )
foutMain.write( '  <head>\n' )
foutMain.write( '    <link rel="stylesheet" type="text/css" href="style.css">\n' )
foutMain.write( '    <link rel="stylesheet" type="text/css" href="slideshow.css">\n' )
foutMain.write( '    <title>MainPage</title>\n\n' )

foutMain.write( '    <style>\n\n' )

foutMain.write( '      body {\n' )
foutMain.write( '        text-align: center;\n' )
foutMain.write( '      }\n\n')

foutMain.write( '    </style>\n' )
foutMain.write( '  </head>\n\n' )

foutMain.write( '  <body>\n' )

#foutMain.write( '      <script src=\'slideshow.js\'></script>\n\n' )


# For each individual
# ~~~~~~~~~~~~~~~~~~~

finCSV = open( 'people.csv', 'rb')
csvReader = csv.reader( finCSV, delimiter=',', quotechar='|')

profiles = []

for row in csvReader:

    sName     = row[0]
    fName     = row[1]
    projTitle = row[2]
    email     = row[3]
    website   = row[4]

    print sName, fName

    # Make relevant directories
    
    directory = os.path.join( 'individuals', sName ).replace( '\'', '_' )
    
    if not os.path.exists( directory ):
        os.makedirs( directory )

    if not os.path.exists( os.path.join( directory, 'profile' ) ):
        os.makedirs( os.path.join( directory, 'profile' ) )

    if not os.path.exists( os.path.join( directory, 'text' ) ):
        os.makedirs( os.path.join( directory, 'text' ) )

    if not os.path.exists( os.path.join( directory, 'images' ) ):
        os.makedirs( os.path.join( directory, 'images' ) )

    dirContent = os.path.join( '/Users/john/Documents/UAL-LCC/MAP17.Website.Content',
                               sName ).replace( '\'', '_' )

        
    # Create a random text document if none exists

    fileStatement = os.path.join( dirContent, 'StatementText', 'statement.txt' )
    
    if not os.path.exists( fileStatement ):

        foutStatement = open( fileStatement, 'wb')

        for iParagraph in range( 3 ):
            for iSentence in range( random.randint( 3, 10 ) ):
                for iWord in range( random.randint( 5, 20 ) ):        

                    word = "".join( random.choice(string.letters)
                                    for i in xrange( random.randint( 1, 15 ) ) )

                    foutStatement.write( ' ' + word )
                foutStatement.write( '.' )
            foutStatement.write( '\n\n' )
                    
        foutStatement.close()
        
    # Update the sidebar menu
        
    fileIndex = os.path.join( directory, 'index.html' )
    
    if ( flgNonModal ):
    
        foutMenu.write( '      <li><a href="{:s}" target="_parent">{:s} {:s}</a></li>\n'.format( fileIndex,
                                                                                                   fName,
                                                                                                   sName ) )
    else:

        foutMenu.write( '      <li><div class="container" onClick="pop({:s})">'.format( "'" + fileIndex + "'" ) )
        foutMenu.write( '{:s} {:s}'.format( fName, sName ) )
        foutMenu.write( '</div></li>\n'.format( fName, sName ) )
        
        
    # Create a page for each individual
    
    foutIndividual = open( fileIndex, 'wb')

    foutIndividual.write( '<!DOCTYPE html>\n\n' )
    foutIndividual.write( '<html>\n' )
    foutIndividual.write( '  <head>\n' )
    foutIndividual.write( '    <link rel="stylesheet" type="text/css" href="../../style.css">\n' )
    foutIndividual.write( '    <link rel="stylesheet" type="text/css" href="../slideshow.css">\n' )
    foutIndividual.write( '    <script src="../slideshow.js"></script>\n' )
    foutIndividual.write( '    <title>{:s} {:s}</title>\n'.format( fName, sName ) )

    foutIndividual.write( '    <style>\n' )

    foutIndividual.write( '      body {\n' )
    foutIndividual.write( '        background-color: white;\n' )
    foutIndividual.write( '      }\n\n')

    foutIndividual.write( '      a:link {\n' )
    foutIndividual.write( '        color: black;\n' )
    foutIndividual.write( '      }\n\n')

    foutIndividual.write( '      div {\n' )
    foutIndividual.write( '        width: 500px;\n' )
    foutIndividual.write( '        height: 100%;\n' )
    foutIndividual.write( '        margin: auto;\n' )
    foutIndividual.write( '      }\n' )

    foutIndividual.write( '      p {\n' )
    foutIndividual.write( '        text-indent: 0px;\n' )
    foutIndividual.write( '      }\n' )

    foutIndividual.write( '    </style>\n' )

    foutIndividual.write( '  </head>\n\n' )
    
    foutIndividual.write( '  <body>\n\n' )

    if ( flgNonModal ):
        foutIndividual.write( '    <span class="close" onClick="goBack()" style="padding-top:0px; padding-right:20px;">&times;</span>\n' )

    foutIndividual.write( '    <h2 align=center><i>{:s}</i></h2>\n\n'.format( projTitle ) )
    foutIndividual.write( '    <h3 align=center>{:s} {:s}</h3>\n\n'.format( fName, sName ) )


    # Create the image slideshow

    fileImages = []
    for suffix in imSuffixes:
        fileImages.extend( glob.glob( os.path.join( dirContent, 'OptionalSelectedImages', suffix ) ) )

    nImages = len( fileImages )
    
    foutIndividual.write( '    <div class="slideshow-container">\n\n' )

    for iImage, fileSrcImage in zip( range( nImages ), fileImages ):

        fileDestImage = os.path.join( directory, 'images', os.path.basename( fileSrcImage ) )
        
        if ( ( not os.path.exists( fileDestImage ) ) or
             ( os.stat( fileSrcImage ).st_mtime - os.stat( fileDestImage ).st_mtime > 1 ) ):

            command = 'convert "{:s}" -resize 800x800 +repage -gravity center -extent 800x800 "{:s}"'.format( fileSrcImage, fileDestImage )
            print 'Copying:', fileSrcImage, 'to', fileDestImage
            print command

            os.system( command )
            
        foutIndividual.write( '    <div class="mySlides fade">\n' )
        foutIndividual.write( '      <div class="numbertext">{:d} of {:d}</div>\n'.format( 1 + iImage,
                                                                                           nImages ) )
        foutIndividual.write( '      <img src="../../{:s}" style="width:100%;">\n'.format( fileDestImage ) )
        #foutIndividual.write( '      <div class="text">Figure {:d}</div>\n'.format( 1 + iImage ) )
        foutIndividual.write( '    </div>\n\n' )


    foutIndividual.write( '    <a class="prev" onclick="plusSlides(-1)"><</a>\n' )
    foutIndividual.write( '    <a class="next" onclick="plusSlides(1)">></a>\n\n' )

    foutIndividual.write( '    </div>\n' )
    foutIndividual.write( '    <br>\n\n' )

        
    foutIndividual.write( '    <div style="text-align:center">\n' )

    for iImage in range( nImages ):
        foutIndividual.write( '      <span class="dot" onclick="currentSlide({:d})"></span> \n'.format( iImage + 1 ) )

    foutIndividual.write( '    </div>\n\n' )
    foutIndividual.write( '    <p>\n\n' )

    
    foutIndividual.write( '    <script>\n' )

    if ( flgNonModal ):
        foutIndividual.write( '      function goBack() {window.history.back();};\n\n')    

    foutIndividual.write( '      showSlides(slideIndex);\n' )
    foutIndividual.write( '    </script>\n\n' )


    # Import artist's statement

    finStatement = open( fileStatement, 'rb')
    txtStatement = finStatement.read()
    splat = txtStatement.split("\n")

    foutIndividual.write( '    <div>\n\n' )
    
    for paragraph in splat:

        if len( paragraph ) > 1:
            foutIndividual.write( '      <p>' )
            foutIndividual.write( paragraph )
            foutIndividual.write( '\n\n' )
        
    finStatement.close()
    
    foutIndividual.write( '      <p>\n\n' )
    foutIndividual.write( '    </div>\n\n' )

        
    # Add email and website

    foutIndividual.write( '    <h4 align=center><a href="mailto:{:s}">{:s}</a></h4>\n\n'.format( email,
                                                                                                 email ) )
    foutIndividual.write( '    <h4 align=center><a href="{:s}" target="top">{:s}</a></h4>\n\n'.format( website,
                                                                                                       website ) )
    
    foutIndividual.write( '\n  </body>\n' )
    foutIndividual.write( '</html>\n' )

    foutIndividual.close()        

    
    # Create the profile thumbnail images

    filesProfile = []
    for suffix in imSuffixes:
        filesProfile.extend( glob.glob( os.path.join( dirContent, 'ThumbnailImage', suffix ) ) )

    if ( len( filesProfile ) < 1 ):
        print 'ERROR: No profile image found in:', os.path.join( dirContent, 'ThumbnailImage' )
        sys.exit(0)

    fileProfile = filesProfile[0]

    fileThumb     = os.path.join( directory, 'profile', 'Thumb.gif' )

    print fileProfile, '->', fileThumb
    
    command = 'convert "{:s}" -resize 256x256^ -gravity center -crop 256x256+0+0 +repage "{:s}"'.format( fileProfile, fileThumb )

    Commands.ExecuteCommand( [ fileThumb ],
                             [ fileProfile ],
                             [ command ],
                             'Creating: ' + fileThumb )

    if ( flgNonModal ):

        foutMain.write( '      <div class="container">\n' )
        foutMain.write( '        <a target="_parent" href="{:s}">\n'.format( fileIndex ) )
        foutMain.write( '          <img src="{:s}" alt="{:s}" class="image">\n'.format( fileThumb,
                                                                                        sName ) )
        foutMain.write( '        <div class="overlay">\n' )
        foutMain.write( '          <div class="text">{:s}\n{:s}</div>\n'.format ( fName.replace( ' ', '\n' ),
                                                                                  sName.replace( ' ', '\n' ) ) )
        foutMain.write( '        </div>\n' )
        foutMain.write( '        </a>\n' )
        foutMain.write( '      </div>\n' )
        
    else:
        
        foutMain.write( '      <div class="container" onClick="pop({:s})">\n'.format( "'" + fileIndex + "'" ) )
        foutMain.write( '        <img src="{:s}" alt="{:s}" class="image">\n'.format( fileThumb,
                                                                                  sName ) )
        foutMain.write( '        <div class="overlay">\n' )
        foutMain.write( '          <div class="text">{:s}\n{:s}</div>\n'.format ( fName.replace( ' ', '\n' ),
                                                                              sName.replace( ' ', '\n' ) ) )
        foutMain.write( '        </div>\n' )
        foutMain.write( '      </div>\n\n' )



if ( not flgNonModal ):
    
    foutMain.write( '      <!-- The Modal -->\n' )
    foutMain.write( '      <div id="TheModal" class="modal">\n' )
    foutMain.write( '        <div class="modal-content">\n' )
    foutMain.write( '          <span class="close" onClick="hide()" style="padding-top:5px; padding-right:10px;">&times;</span>\n' )
    foutMain.write( '          <div id="TheModalContent" style="width:100%; height:90%;"></div>\n' )
    foutMain.write( '        </div>\n' )
    foutMain.write( '      </div>\n\n' )

    foutMain.write( '      <script src=\'modal.js\'></script>\n\n' )
     
foutMain.write( '  </body>\n' )
    

# Clean up
# ~~~~~~~~

foutMain.write( '</html>\n' )
foutMain.close()        

foutMenu.write( '\n    </ul>\n' )
foutMenu.write( '\n  </body>\n' )
foutMenu.write( '</html>\n' )
foutMenu.close()        

finCSV.close()
