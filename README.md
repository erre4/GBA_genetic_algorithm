# Description:
This report provides a simple code for a little 2Dshooting game runnable on a GBA emulator and devices supplied with gba cartridge readers.
The enemy in the game has been trained with a NEAT algorithm on a computer.

Work in progress...

# Setting Up the Environment:

In this section I will explain what you will need to compile and run the code provided in the repo.

To run the code on hardware devices such as the gameboy advance, 
you will need to compile the code so that the binary file can be executed by the device architecture.

The GBA runs on a ARM7tdmi RISC chip at 16.78 MHz (224 cycles/second). It is a 32bit chip that can run on two different instruction sets. 
First, there's is ARM code, which is a set of 32bit instructions. Then there's THUMB, which uses 16bit instructions. THUMB instructions are a subset of the ARM instruction set.

So, first of all you will need to download devkitARM (DKA), an ARM cross-compiler, based on the GCC toolchain.
Then you will need of libgba, a set of basic types, macros and functions for use in GBA development.

These two download are sufficient to compile the code.
To run the code you will need of a gba emulator, i'm currently using VisualBoy advance.

devkitARM is available for Mac, Windows and Linux, you can find it here:
```
https://sourceforge.net/projects/devkitpro/
```
I only tried the linux download and i raccomend to download the .pl file.

for those who have downloaded the .pl file

you can run it with:

- pearl devkitARMupdate.pl

When the download is finished you have to follow the istructions appearing on the bash to save the paths of devkitpro and devkitArm.
This passage is not strictly necessary, but if you want a well made Makefile this passage could be useful.
The .pl file already contains everything needed for compiling, even libgba

for those who have downloaded the .tar file

open the bash and then:

- cd /opt/devkitpro
- tar -xvjf <file you downloaded>

Now you have to download libgba separately and ou can download it here:

- https://sourceforge.net/projects/devkitpro/files/libgba/libgba-20150106.tar.bz2/download

then, in the devkitPro directory:

- mkdir libgba
- cd libgba
- tar -xvjf <libgba you downloaded>

Then:

- export DEVKITPRO=/opt/devkitpro
- export DEVKITARM=$DEVKITPRO/devkitARM

for the paths. (as i said before: is not strictly necessary, but if you want a well made Makefile this passage could be useful).

Now you have to download the emulator for gba:

- sudo apt-get install visualboyadvance-gtk

Is possible that during the compilation you can have someproblems and a massage like this could appear:

- whiite:/opt/devkitpro/examples/wii# make
- make[1]: Entering directory `/opt/devkitpro/examples/wii/audio'
- make[2]: Entering directory `/opt/devkitpro/examples/wii/audio/modplay'
- linking ... modplay.elf
- /opt/devkitpro/devkitPPC/lib/gcc/powerpc-eabi/4.6.3/../../../../powerpc-eabi/bin/ld: cannot find -lwiiuse
- /opt/devkitpro/devkitPPC/lib/gcc/powerpc-eabi/4.6.3/../../../../powerpc-eabi/bin/ld: cannot find -lbte
- /opt/devkitpro/devkitPPC/lib/gcc/powerpc-eabi/4.6.3/../../../../powerpc-eabi/bin/ld: cannot find -lmodplay
- /opt/devkitpro/devkitPPC/lib/gcc/powerpc-eabi/4.6.3/../../../../powerpc-eabi/bin/ld: cannot find -laesnd
- /opt/devkitpro/devkitPPC/lib/gcc/powerpc-eabi/4.6.3/../../../../powerpc-eabi/bin/ld: cannot find -logc
- collect2: ld returned 1 exit status
- make[3]: *** [/opt/devkitpro/examples/wii/audio/modplay/modplay.elf] Error 1
- make[2]: *** [build] Error 2
- make[2]: Leaving directory `/opt/devkitpro/examples/wii/audio/modplay'
- make[1]: *** [all] Error 1
- make[1]: Leaving directory `/opt/devkitpro/examples/wii/audio'
- make: *** [all] Error 1

or something like that, then you have to download the .pl file, and you can follow the istructions described above.

Now you have your environment to compile and run the .gba code!

# How to Compile:

during the compilation you can type the following lines on the bash:

- # Compile first.c to first.o
- arm-none-eabi-gcc -mthumb -mthumb-interwork -c first.c
- 
- # Link first.o (and standard libs) to first.elf
- arm-none-eabi-gcc -specs=gba.specs -mthumb -mthumb-interwork first.o -o first.elf
- 
- # Strip to binary-only
- arm-none-eabi-objcopy -O binary first.elf first.gba
- 
- # Fix header
- gbafix first.gba

or, simply using the makefile. (it will work if you have exported correctly the paths of devkitpro and devkitarm):

- make

# How to run

- gvba first.gba






 

