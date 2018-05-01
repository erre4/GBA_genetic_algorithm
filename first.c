#include "toolbox.h"
#include "drawing.h"

/*speed should not be changed*/
#define SPEED 2
#define SIZE 6
#define FRAME 7
#define PLAYER_SPAWN 65
#define CPU_SPAWN 180

inline void vid_flip(){
	REG_DISPCNT ^= DCNT_PAGE;
}

inline void drawing_up(int* x1, int* x2, int* y1, int* y2, int* k){
	
		*y1-=2;
		*y2-=2;
		
		m4_fully_rectangle(*x1,*y1,*x1+SPEED,*y2,1);
		m4_fully_rectangle(*x2-SPEED,*y1,*x2,*y2,1);
		m4_fully_rectangle(*x1+SPEED,*y1,*x2-SPEED,*y1+2*SPEED,1);
		
		vid_flip();
		
		if(*k) vid_page = vid_second_mem;
		else vid_page = vid_mem;
		
		*k = *k ^ 1;
		
		
		m4_fully_rectangle(*x1,*y2-(SPEED-1),*x2,*y2+SPEED,0);
		m4_fully_rectangle(*x1,*y1+SPEED,*x1+(SPEED-1),*y2-SPEED,0);
		m4_fully_rectangle(*x2-(SPEED-1),*y1+SPEED,*x2,*y2-SPEED,0);
}

inline void drawing_down(int* x1, int* x2, int* y1, int* y2, int* k){
	
		*y1+=2;
		*y2+=2;
		
		m4_fully_rectangle(*x1,*y1,*x1+SPEED,*y2,1);
		m4_fully_rectangle(*x2-SPEED,*y1,*x2,*y2,1);
		m4_fully_rectangle(*x1+SPEED,*y2-2*SPEED,*x2-SPEED,*y2,1);
		
		vid_flip();
		
		if(*k) vid_page = vid_second_mem;
		else vid_page = vid_mem;
		
		*k = *k ^ 1;
		
		
		m4_fully_rectangle(*x1,*y1-SPEED,*x2,*y1+(SPEED-1),0);
		m4_fully_rectangle(*x1,*y1+SPEED,*x1+(SPEED-1),*y2-SPEED,0);
		m4_fully_rectangle(*x2-(SPEED-1),*y1+SPEED,*x2,*y2-SPEED,0);
}

inline void drawing_left(int* x1, int* x2, int* y1, int* y2, int* k){
	
		*x1-=2;
		*x2-=2;
		
		m4_fully_rectangle(*x1,*y1,*x2,*y1+SPEED,1);
		m4_fully_rectangle(*x1,*y2-SPEED,*x2,*y2,1);
		m4_fully_rectangle(*x1,*y1+SPEED,*x1+(SPEED*2),*y2-SPEED,1);
		
		vid_flip();
		
		if(*k) vid_page = vid_second_mem;
		else vid_page = vid_mem;
		
		*k = *k ^ 1;
		
		
		m4_fully_rectangle(*x2-(SPEED-1),*y1,*x2+SPEED,*y2,0);
		m4_fully_rectangle(*x1+SPEED,*y1,*x2-SPEED,*y1+(SPEED-1),0);
		m4_fully_rectangle(*x1+SPEED,*y2-(SPEED-1),*x2-SPEED,*y2,0);
}

inline void drawing_right(int* x1, int* x2, int* y1, int* y2, int* k){
	
		*x1+=2;
		*x2+=2;
		
		m4_fully_rectangle(*x1,*y1,*x2,*y1+SPEED,1);
		m4_fully_rectangle(*x1,*y2-SPEED,*x2,*y2,1);
		m4_fully_rectangle(*x2-2*SPEED,*y1+SPEED,*x2,*y2-SPEED,1);
		
		vid_flip();
		
		if(*k) vid_page = vid_second_mem;
		else vid_page = vid_mem;
		
		*k = *k ^ 1;
		
		
		m4_fully_rectangle(*x1-SPEED,*y1,*x1+(SPEED-1),*y2,0);
		m4_fully_rectangle(*x1+SPEED,*y1,*x2-SPEED,*y1+(SPEED-1),0);
		m4_fully_rectangle(*x1+SPEED,*y2-(SPEED-1),*x2-SPEED,*y2,0);
}

int main()
{
	if(PLAYER_SPAWN<0 || PLAYER_SPAWN+SIZE > SCREEN_HEIGHT || CPU_SPAWN < 0 || CPU_SPAWN+SIZE > SCREEN_HEIGHT || SPEED != 2) exit(1);
	
    int x1 = PLAYER_SPAWN, x2 = x1+SIZE, y1 = PLAYER_SPAWN, y2 = y1+SIZE, k = 0, frame;
    
    
	/*activating mode 4*/
    REG_DISPCNT= DCNT_MODE4 | DCNT_BG2;
    
    /*THE LOCATION AT PALLETTE[1] = RED*/
    u16 *dst= (u16*)PALLETTE;
    dst[1] = RGB15(31, 0, 0);
	
	/*drawing a fully red rectangle on first page*/
    m4_fully_rectangle(x1,y1,x2,y2,1);
    
    /*pointing to the second page*/
    vid_page = vid_second_mem;
    
    /*drawing a fully red rectangle on second page*/
    m4_fully_rectangle(x1+SPEED,y1+SPEED,x2-SPEED,y2-SPEED,1);
    
    while(1){
        vid_vsync();
      
		//checking the keys
        key_poll();
        
        // check state of each button
           
        if(key_hit(KEY_UP) && y1>1)
        
			drawing_up(&x1, &x2, &y1, &y2, &k);
			
		else if(key_held(KEY_UP) && y1>1){
			for(frame = 0; frame < FRAME; frame++);
			drawing_up(&x1, &x2, &y1, &y2, &k);
		}
		
		else if(key_hit(KEY_DOWN) && y2<159)
        
			drawing_down(&x1, &x2, &y1, &y2, &k);
			
		else if(key_held(KEY_DOWN) && y2<159){
			for(frame = 0; frame < FRAME; frame++);
			drawing_down(&x1, &x2, &y1, &y2, &k);
		}
		
		else if(key_hit(KEY_LEFT) && x1>1)
        
			drawing_left(&x1, &x2, &y1, &y2, &k);
			
		else if(key_held(KEY_LEFT) && x1>1){
			for(frame = 0; frame < FRAME; frame++);
			drawing_left(&x1, &x2, &y1, &y2, &k);
		}
		
		else if(key_hit(KEY_RIGHT) && x2<239)
        
			drawing_right(&x1, &x2, &y1, &y2, &k);
			
		else if(key_held(KEY_RIGHT) && x2<239){
			for(frame = 0; frame < FRAME; frame++);
			drawing_right(&x1, &x2, &y1, &y2, &k);
		}		
		 
    }
    return 0;
}
