package test.Codility_java;


	public class BinaryGap {
		public static void main(String[] args){
			System.out.println(binarygap(32));
			
		   }
		public static int binarygap(int n) {
			int max_gap = 0;
			int counter = 0;
			int temCounter = 0;
			String bin_str = Integer.toBinaryString(n);
			for(int i = 0; i< bin_str.length();i++) {
				if (bin_str.charAt(i) == '0') {
					counter++;}
				else{
					if (counter > max_gap) {
						max_gap = counter;
						counter = 0;
					}	
				}
			
			
		
		}
			return max_gap;

}}
