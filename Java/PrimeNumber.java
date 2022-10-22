import java.util.Scanner;
class PrimeNumber{
    public static void main(String[] args) {
        boolean flag = true;
        int half = 0;
        System.out.println("Enter a number to find whether it is a prime or Not :-");
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        half = number/2;
        if(number > 1){
            for(int num = 2;num <= half;num++){
                if(number % num == 0){
                    System.out.println("It is not a Prime number");
                    flag = false;
                    break;
                }
            }
            if(flag){
                System.out.println(number + " is a Prime Number");
            }
        }else{
            System.out.println("It is not a Prime number");
        }
    }
}