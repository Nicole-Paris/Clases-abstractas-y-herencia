import { PayMentMethod } from "./PayMentMethod";

export class BitcointPayMent extends PayMentMethod{
    pay(amount){
        console.log("Pago con Bitcoin");
    }
}