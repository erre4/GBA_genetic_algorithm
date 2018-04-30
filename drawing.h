#include "toolbox.h"

/*drawing a line in  mode 3*/
void m3_line(int x1, int y1, int x2, int y2,COLOR clr){
	int dx, dy, i, k1 = 1, k2 = 1;
	
	if(x2>x1) dx = x2-x1;
	else{
		dx = x1-x2;
		k1 = -1;
	}
	
	if(y2>y1) dy = y2-y1;
	else{
		dy = y1-y2;
		k2 = -1;
	}
	
	if(dx == 0){
		for(i = 0; i < dy +1; i++){
			m3_plot(x1, y1 + k2*i, clr);
		}
	}
	
	else if(dy == 0){
		for(i = 0; i < dx +1; i++){
			m3_plot(x1 + k1*i, y1, clr);
		}
	}
	
	else{
		for(i = 0; i < dx +1; i++){
			m3_plot(x1 +k1*i, y1 + k2*i, clr);
		}
	}
}

/*drawing an empty rectangle in mode 3*/
void m3_empty_rectangle(int x1, int y1, int x2, int y2, COLOR clr){
	
	if(x1 == x2 && y1 == y2)
		m3_plot(x1, y1, clr);
		
	else if(x1 == x2)
		m3_line(x1,y1,x1,y2,clr);
	
	else if (y1 == y2)
		m3_line(x1,y1,x2,y1,clr);
	
	else{
		m3_line(x1,y1,x2,y1,clr);
		m3_line(x1,y1,x1,y2,clr);
		m3_line(x1,y2,x2,y2,clr);
		m3_line(x2,y1,x2,y2,clr);
	}

}

/*drawing a full rectangle in mode 3*/
void m3_fully_rectangle(int x1, int y1, int x2, int y2, COLOR clr){
	
	int min, dx, dy, i, k1 = 1, k2 = 1;
	
	if(x2>x1) dx = x2-x1;
	else{
		dx = x1-x2;
		k1 = -1;
	}
	
	if(y2>y1) dy = y2-y1;
	else{
		dy = y1-y2;
		k2 = -1;
	}
	
	if(dx<=dy) min = dx;
	else
		min = dy;
	
	for(i = 0; i < min; i++){
		m3_empty_rectangle(x1 + i*k1,y1 +i*k2,x2 - i*k1,y2 - i*k2,clr);
	}

	

}

/*drawing a line in  mode 4*/
void m4_line(int x1, int y1, int x2, int y2,u8 clr){
	int dx, dy, i, k1 = 1, k2 = 1;
	
	if(x2>x1) dx = x2-x1;
	else{
		dx = x1-x2;
		k1 = -1;
	}
	
	if(y2>y1) dy = y2-y1;
	else{
		dy = y1-y2;
		k2 = -1;
	}
	
	if(dx == 0){
		for(i = 0; i < dy +1; i++){
			m4_plot(x1, y1 + k2*i, clr);
		}
	}
	
	else if(dy == 0){
		for(i = 0; i < dx +1; i++){
			m4_plot(x1 + k1*i, y1, clr);
		}
	}
	
	else{
		for(i = 0; i < dx +1; i++){
			m4_plot(x1 +k1*i, y1 + k2*i, clr);
		}
	}
}

/*drawing an empty rectangle in mode 4*/
void m4_empty_rectangle(int x1, int y1, int x2, int y2, u8 clr){
	
	if(x1 == x2 && y1 == y2)
		m4_plot(x1, y1, clr);
		
	else if(x1 == x2)
		m4_line(x1,y1,x1,y2,clr);
	
	else if (y1 == y2)
		m4_line(x1,y1,x2,y1,clr);
	
	else{
		m4_line(x1,y1,x2,y1,clr);
		m4_line(x1,y1,x1,y2,clr);
		m4_line(x1,y2,x2,y2,clr);
		m4_line(x2,y1,x2,y2,clr);
	}
}

/*drawing a full rectangle in mode 4*/
void m4_fully_rectangle(int x1, int y1, int x2, int y2, u8 clr){
	
	int min, dx, dy, i, k1 = 1, k2 = 1;
	
	if(x2>x1) dx = x2-x1;
	else{
		dx = x1-x2;
		k1 = -1;
	}
	
	if(y2>y1) dy = y2-y1;
	else{
		dy = y1-y2;
		k2 = -1;
	}
	
	if(dx<=dy) min = dx;
	else
		min = dy;
	
	for(i = 0; i < min; i++){
		m4_empty_rectangle(x1 + i*k1,y1 +i*k2,x2 - i*k1,y2 - i*k2,clr);
	}

	

}



