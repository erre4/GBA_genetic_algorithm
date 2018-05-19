# Description:
This report provides a simple code for a little 2Dshooting game runnable on a GBA emulator and devices supplied with gba cartridge readers.
The enemy in the game has been trained with a NEAT algorithm on a computer.

No sprite or tiles are used, but for the simplicity of the graphics has been used the mode_4

Work in progress...

# Setting Up the Environment:

In this section I will explain what you will need to compile and run the code provided in the repo.

To run the code on hardware devices such as the gameboy advance, 
you will need to compile the code so that the binary file can be executed by the device architecture.

The GBA runs on a ARM7tdmi RISC chip at 16.78 MHz (224 cycles/second). It is a 32bit chip that can run on two different instruction sets. 
First, there's is ARM code, which is a set of 32bit instructions. Then there's THUMB, which uses 16bit instructions. THUMB instructions are a subset of the ARM instruction set.

So, first of all you will need to download devkitARM (DKA), an ARM cross-compiler, based on the GCC toolchain.
Then you will need of libgba, a set of basic types, macros and functions for use in GBA development.

These two downloads are sufficient to compile the code.
To run the code you will need of a gba emulator, i'm currently using VisualBoy advance.

devkitARM is available for Mac, Windows and Linux, you can find it here:


- https://sourceforge.net/projects/devkitpro/


For linux users, i raccomend these operations, open the terminal and paste these lines:

```
sudo mkdir -p /opt/devkitpro
sudo chmod 777 /opt/devkitpro
```

Download this file:

- https://sourceforge.net/projects/devkitpro/files/devkitARM/devkitARM_r47/devkitARM_r47-x86_64-linux.tar.bz2/download

and then,

```
cd /opt/devkitpro
tar -xvjf <file you downloaded>
```
  
after that, download this file:

- https://sourceforge.net/projects/devkitpro/files/libgba/0.5.0/libgba-0.5.0.tar.bz2/download

and then in deviktpro folder:

```
mkdir libgba
cd libgba
tar -xvjf <last file downloaded>
```
  
after that export the path of devkitPro and devkitARM

```
export DEVKITPRO=/opt/devkitpro
export DEVKITARM=$DEVKITPRO/devkitARM
```

To download VisualBoy:

```
sudo apt-get install visualboyadvance-gtk
```

Now you have your environment to compile and run .gba code!

# The algorithm:

The algorithm used is NEAT, a genetic algorithm implemented in python. In neat directory you can actually see the modules to run and train a genetic network.

# How to Compile C code:

during the compilation you can type the following lines on the bash:

- Compile first.c to first.o
```
arm-none-eabi-gcc -mthumb -mthumb-interwork -c first.c
``` 
- Link first.o (and standard libs) to first.elf

```
arm-none-eabi-gcc -specs=gba.specs -mthumb -mthumb-interwork first.o -o first.elf
```

- Strip to binary-only
```
arm-none-eabi-objcopy -O binary first.elf first.gba
```

- Fix header
```
gbafix first.gba
```

or, simply you can use the makefile. (it will work if you have correctly exported the paths of devkitpro and devkitarm):

```
make
```
# How to run .gba

```
gvba first.gba
```



# Linkography:

GBA tutorial:
- http://www.coranac.com/tonc/text/toc.htm

GBA hardware specifications:
- https://www.cs.rit.edu/~tjh8300/CowBite/CowBiteSpec.htm

NEAT algorithm paper

- http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf

