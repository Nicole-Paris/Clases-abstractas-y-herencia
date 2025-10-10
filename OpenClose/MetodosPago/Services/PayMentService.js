export class PayMentService {
    serviceProcess(paymentMethod, amount) {
        paymentMethod.pay(amount);
    }
}