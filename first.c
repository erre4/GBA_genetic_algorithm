#include "toolbox.h"
#include "drawing.h"

/*speed should not be changed*/
#define SPEED 2
#define PLAYER_SIZE 6
#define BULLET_SIZE 2
#define FRAME 7
#define PLAYER_SPAWN 65
#define CPU_SPAWN 140
#define BULLETS 10




 
 


inline void vid_flip(){
    REG_DISPCNT ^= DCNT_PAGE;
}


inline void drawing_up(int* x1, int* x2, int* y1, int* y2, int* k, int RESIZE_HIT, int RESIZE_FLAG){
        *y1-=SPEED;
        *y2-=SPEED;

        m4_fully_rectangle(*x1,*y1,*x2,*y2,1);
        
        vid_flip();
        
        if(*k) vid_page = vid_second_mem;
        else vid_page = vid_mem;
        
        *k = *k ^ 1;
        
        if(RESIZE_HIT && !RESIZE_FLAG){
            *x1 -= PLAYER_SIZE/2;
            *x2 += PLAYER_SIZE/2;
            *y1 -= PLAYER_SIZE/2;
            *y2 += PLAYER_SIZE/2;
            
            m4_fully_rectangle(*x1,*y1+SPEED,*x2,*y2+SPEED,0);
            
            *x1 += PLAYER_SIZE/2;
            *x2 -= PLAYER_SIZE/2;
            *y1 += PLAYER_SIZE/2;
            *y2 -= PLAYER_SIZE/2;
        }
        
        else{
            m4_fully_rectangle(*x1,*y1+SPEED,*x2,*y2+SPEED,0);
        }        
}

inline void drawing_down(int* x1, int* x2, int* y1, int* y2, int* k, int RESIZE_HIT, int RESIZE_FLAG){
    
        *y1+=SPEED;
        *y2+=SPEED;
        
        m4_fully_rectangle(*x1,*y1,*x2,*y2,1);
        
        vid_flip();
        
        if(*k) vid_page = vid_second_mem;
        else vid_page = vid_mem;
        
        *k = *k ^ 1;
        if(RESIZE_HIT && !RESIZE_FLAG){
            *x1 -= PLAYER_SIZE/2;
            *x2 += PLAYER_SIZE/2;
            *y1 -= PLAYER_SIZE/2;
            *y2 += PLAYER_SIZE/2;
            
            m4_fully_rectangle(*x1,*y1-SPEED,*x2,*y2-SPEED,0);
            
            *x1 += PLAYER_SIZE/2;
            *x2 -= PLAYER_SIZE/2;
            *y1 += PLAYER_SIZE/2;
            *y2 -= PLAYER_SIZE/2;
        }
        
        else{
            m4_fully_rectangle(*x1,*y1-SPEED,*x2,*y2-SPEED,0);
        }
}

inline void drawing_left(int* x1, int* x2, int* y1, int* y2, int* k, int RESIZE_HIT, int RESIZE_FLAG){
    
        *x1-=SPEED;
        *x2-=SPEED;

        m4_fully_rectangle(*x1,*y1,*x2,*y2,1);
        vid_flip();
        
        if(*k) vid_page = vid_second_mem;
        else vid_page = vid_mem;
        
        *k = *k ^ 1;
        if(RESIZE_HIT && !RESIZE_FLAG){
            *x1 -= PLAYER_SIZE/2;
            *x2 += PLAYER_SIZE/2;
            *y1 -= PLAYER_SIZE/2;
            *y2 += PLAYER_SIZE/2;
            
            m4_fully_rectangle(*x1+SPEED,*y1,*x2+SPEED,*y2,0);
            
            *x1 += PLAYER_SIZE/2;
            *x2 -= PLAYER_SIZE/2;
            *y1 += PLAYER_SIZE/2;
            *y2 -= PLAYER_SIZE/2;
        }
        
        else{
            m4_fully_rectangle(*x1+SPEED,*y1,*x2+SPEED,*y2,0);
        }
}

inline void drawing_right(int* x1, int* x2, int* y1, int* y2, int* k, int RESIZE_HIT, int RESIZE_FLAG){
    
        *x1+=SPEED;
        *x2+=SPEED;
        
        m4_fully_rectangle(*x1,*y1,*x2,*y2,1);
        vid_flip();
        
        if(*k) vid_page = vid_second_mem;
        else vid_page = vid_mem;
        
        *k = *k ^ 1;
        if(RESIZE_HIT && !RESIZE_FLAG){
            *x1 -= PLAYER_SIZE/2;
            *x2 += PLAYER_SIZE/2;
            *y1 -= PLAYER_SIZE/2;
            *y2 += PLAYER_SIZE/2;
            
            m4_fully_rectangle(*x1-SPEED,*y1,*x2-SPEED,*y2,0);
            
            *x1 += PLAYER_SIZE/2;
            *x2 -= PLAYER_SIZE/2;
            *y1 += PLAYER_SIZE/2;
            *y2 -= PLAYER_SIZE/2;
        }
        
        else{
            m4_fully_rectangle(*x1-SPEED,*y1,*x2-SPEED,*y2,0);
    }
}

int main()
{
    if(PLAYER_SPAWN<0 || PLAYER_SPAWN+PLAYER_SIZE > SCREEN_HEIGHT || CPU_SPAWN < 0 || CPU_SPAWN+PLAYER_SIZE > SCREEN_HEIGHT || SPEED != 2) return 1;
    
    int x1 = PLAYER_SPAWN, x2 = x1+PLAYER_SIZE, y1 = PLAYER_SPAWN, y2 = y1+PLAYER_SIZE, k = 0, frame;
    
    int RESIZE_FLAG = 0;
    int RESIZE_HIT = 0;
    
    /*activating mode 4*/
    REG_DISPCNT= DCNT_MODE4 | DCNT_BG2;
    
    /*THE LOCATION AT PALLETTE[1] = RED*/
    u16 *dst= (u16*)PALLETTE;
    dst[1] = RGB15(31, 0, 0);
    /*in somedevices such as ds lite somepixels aren't black so on first page:*/
    m4_fully_rectangle(0,0,240,160,0);

    /*drawing a fully red rectangle on first page*/
    m4_fully_rectangle(x1,y1,x2,y2,1);
    
    /*pointing to the second page*/
    vid_page = vid_second_mem;
    
    /*on second page*/
    m4_fully_rectangle(0,0,240,160,0);

    while(1){
        vid_vsync();
      
        //checking the keys
        key_poll();
        
        // check state of each button
        RESIZE_HIT = 0;
        
        if(!RESIZE_FLAG && key_hit(KEY_R) && x1 > 5 && x2 < 235 && y1 > 5 && y2 < 155){
            
            x1 -= PLAYER_SIZE/2;
            x2 += PLAYER_SIZE/2;
            y1 -= PLAYER_SIZE/2;
            y2 += PLAYER_SIZE/2;
                        
            RESIZE_FLAG ^= 1;
            RESIZE_HIT = 1;
        }
        
        else if(!RESIZE_HIT && RESIZE_FLAG && key_hit(KEY_L)){
            
            x1 += PLAYER_SIZE/2;
            x2 -= PLAYER_SIZE/2;
            y1 += PLAYER_SIZE/2;
            y2 -= PLAYER_SIZE/2;
            
            RESIZE_FLAG ^= 1;
            RESIZE_HIT = 1;
            
        } 
        
        if(key_hit(KEY_UP) && y1>1)
        
            drawing_up(&x1, &x2, &y1, &y2, &k, RESIZE_HIT, RESIZE_FLAG);
        
        else if(key_held(KEY_UP) && y1>1){
            for(frame = 0; frame < FRAME; frame++);
            drawing_up(&x1, &x2, &y1, &y2, &k, RESIZE_HIT, RESIZE_FLAG);
        }
        
        else if(key_hit(KEY_DOWN) && y2<159)
        
            drawing_down(&x1, &x2, &y1, &y2, &k, RESIZE_HIT, RESIZE_FLAG);
            
        else if(key_held(KEY_DOWN) && y2<159){
            for(frame = 0; frame < FRAME; frame++);
            drawing_down(&x1, &x2, &y1, &y2, &k, RESIZE_HIT, RESIZE_FLAG);
        }
        
        else if(key_hit(KEY_LEFT) && x1>1)
        
            drawing_left(&x1, &x2, &y1, &y2, &k, RESIZE_HIT, RESIZE_FLAG);
            
        else if(key_held(KEY_LEFT) && x1>1){
            for(frame = 0; frame < FRAME; frame++);
            drawing_left(&x1, &x2, &y1, &y2, &k, RESIZE_HIT, RESIZE_FLAG);
        }
        
        else if(key_hit(KEY_RIGHT) && x2<238)
        
            drawing_right(&x1, &x2, &y1, &y2, &k, RESIZE_HIT, RESIZE_FLAG);
            
        else if(key_held(KEY_RIGHT) && x2<238){
            for(frame = 0; frame < FRAME; frame++);
            drawing_right(&x1, &x2, &y1, &y2, &k, RESIZE_HIT, RESIZE_FLAG);
        }
        
        else{
            if(RESIZE_HIT){
                if(RESIZE_FLAG){
                    
                     x1 += PLAYER_SIZE/2;
                     x2 -= PLAYER_SIZE/2;
                     y1 += PLAYER_SIZE/2;
                     y2 -= PLAYER_SIZE/2;


                }
                
                else{
                    x1 -= PLAYER_SIZE/2;
                    x2 += PLAYER_SIZE/2;
                    y1 -= PLAYER_SIZE/2;
                    y2 += PLAYER_SIZE/2;

                }
                
                RESIZE_FLAG ^= 1;

            }
        }    
        
         
    }
    return 0;
}
