// toolbox.h: 
//
// === NOTES ===
// * This is a _small_ set of typedefs, #defines and inlines that can 
//   be found in tonclib, and might not represent the 
//   final forms.


#ifndef TOOLBOX_H
#define TOOLBOX_H

// === (from tonc_types.h) ============================================

typedef unsigned char   u8;
typedef unsigned short  u16;
typedef unsigned int    u32;

typedef volatile unsigned short vu16;
typedef u16 COLOR;

#define INLINE static inline


#define MEM_IO      	  0x04000000
#define MEM_VRAM    	  0x06000000
#define MEM_VRAM_2ND_PAGE 0x0600A000
#define MEM_IWRAM   	  0x03000000
#define MEM_EWRAM   	  0x02000000
#define PALLETTE    	  0x05000000

#define REG_DISPCNT     *((volatile u32*)(MEM_IO+0x0000))
#define REG_KEYINPUT    *((volatile u32*)0x04000130)

// Globals to hold the key state
u16 __key_curr=0, __key_prev=0;

#define KEY_A        0x0001
#define KEY_B        0x0002
#define KEY_SELECT   0x0004
#define KEY_START    0x0008
#define KEY_RIGHT    0x0010
#define KEY_LEFT     0x0020
#define KEY_UP       0x0040
#define KEY_DOWN     0x0080
#define KEY_R        0x0100
#define KEY_L        0x0200

#define KEY_MASK     0x03FF

// Polling function
INLINE void key_poll()
{
    __key_prev= __key_curr;
    __key_curr= ~REG_KEYINPUT & KEY_MASK;
}


// Transitional state checks.

// Key is changing state.
INLINE u32 key_transit(u32 key)
{   return ( __key_curr ^  __key_prev) & key;   }

// Key is held (down now and before).
INLINE u32 key_held(u32 key)
{   return ( __key_curr &  __key_prev) & key;  }

// Key is being hit (down now, but not before).
INLINE u32 key_hit(u32 key)
{   return ( __key_curr &~ __key_prev) & key;  }

//Key is being released (up now but down before)
INLINE u32 key_released(u32 key)
{   return (~__key_curr &  __key_prev) & key;  }


// --- REG_DISPCNT defines ---
#define DCNT_MODE0      0x0000
#define DCNT_MODE1      0x0001
#define DCNT_MODE2      0x0002
#define DCNT_MODE3      0x0003
#define DCNT_MODE4      0x0004
#define DCNT_MODE5      0x0005
// layers
#define DCNT_BG0        0x0100
#define DCNT_BG1        0x0200
#define DCNT_BG2        0x0400
#define DCNT_BG3        0x0800
#define DCNT_OBJ        0x1000

#define DCNT_PAGE       0x0010


#define SCREEN_WIDTH   240
#define SCREEN_HEIGHT  160

#define vid_mem  ((u16*)MEM_VRAM)
#define vid_second_mem ((u16*)MEM_VRAM_2ND_PAGE)



u16 *vid_page = vid_mem;     // Point to current frame buffer

/*plotting a dot of a pixel with mode 4(8bpp)*/
INLINE void m4_plot(int x, int y, u8 clrid)
{
    u16 *dst= &vid_page[(y*SCREEN_WIDTH+x)/2];  // Division by 2 due to u8/u16 pointer mismatch!
    if(x&1)
        *dst= (*dst& 0xFF) | (clrid<<8);    // odd pixel
    else
        *dst= (*dst&~0xFF) |  clrid;        // even pixel
}

#define CLR_BLACK   0x0000
#define CLR_RED     0x001F
#define CLR_LIME    0x03E0
#define CLR_YELLOW  0x03FF
#define CLR_BLUE    0x7C00
#define CLR_MAG     0x7C1F
#define CLR_CYAN    0x7FE0
#define CLR_WHITE   0x7FFF

/*given 3 numbers it will give the color*/
INLINE COLOR RGB15(u32 red, u32 green, u32 blue)
{   return red | (green<<5) | (blue<<10);   }

/*waiting for Vdraw e vblank ended*/
#define REG_VCOUNT *(vu16*)0x04000006

void vid_vsync()
{
    while(REG_VCOUNT >= 160);   // wait till VDraw
    while(REG_VCOUNT < 160);    // wait till VBlank
}

#endif // TOOLBOX_H
