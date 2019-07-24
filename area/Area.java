public class Area {
	public static int computeArea(int a, int b, int c, int d, int e, int f, int g, int h) {
		if (  (validate(e,c,a) || validate(f,d,b)) && (validate(g,c,a) || validate(h,d,b))) {
			return (Math.abs(a-c)) * (Math.abs(b-d));
		}
		else if((validate(a,g,e) || validate(b,h,f)) && (validate(c,g,e) || validate(d,h,f))) {	
			return (Math.abs(e-g)) * (Math.abs(f-h));
		}
		else if(e<c && f>b){
			return (Math.abs(a-c)) * (Math.abs(b-d)) + (Math.abs(e-g)) * (Math.abs(f-h)) - (Math.abs(c-e)) * (Math.abs(d-f)) ;
		}
		else {
			return (Math.abs(a-c)) * (Math.abs(b-d)) + (Math.abs(e-g)) * (Math.abs(f-h)) - (Math.abs(g-a)) * (Math.abs(h-b)) ;	
		}
	}
	public static boolean validate (int x, int y, int z ) {
		 return (x>=0) ? (x<=y && x>=z) : (x>=z && x<=y);
	}
}

 