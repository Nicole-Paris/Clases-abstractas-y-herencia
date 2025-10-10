import { PayMentService } from "./PayMentService.js";
import { CreditCardPayMent } from "./models/CreditCardPayMent.js";
import { BitcointPayMent } from "./models/BitcoinPayMent.js";
import { PaypalPayMent } from "./models/PayPalPayMent.js";


const service = new PayMentService();
const CreditCard = new CreditCardPayMent();
const Bitcoin = new BitcointPayMent();
const Paypal = new PaypalPayMent();

service.serviceProcess(CreditCard, 200);
service.serviceProcess(Paypal, 500);
service.serviceProcess(Bitcoin, 1000);