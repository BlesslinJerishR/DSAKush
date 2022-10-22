import java.util.Scanner;
public class SalaryBonus {
    public static void main(String[] args) {
        int salary;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the salary :-");
        salary = sc.nextInt();
        if (salary > 10000){
            salary += 2000;
            System.out.println("Your Salary with Bonus is "+ salary);
        }
        else{
            salary += 1000;
            System.out.println("Your Salary with Bonus is "+ salary);
        }
    }
}
