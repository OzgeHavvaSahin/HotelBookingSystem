namespace nigar_payment_service.Events;

public class PaymentRefundedEvent
{
    public long BookingId { get; set; }
    public long PaymentId     { get; set; }
}