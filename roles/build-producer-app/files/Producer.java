import com.rabbitmq.client.BuiltinExchangeType;
import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.Channel;

public class Producer {

  private static final String EXCHANGE_NAME = "hello-exchange";

  public static void main(String[] argv) throws Exception {
    ConnectionFactory factory = new ConnectionFactory();
    factory.setHost("localhost");
	factory.setUsername("guest");
	factory.setPassword("guest");
    Connection connection = factory.newConnection();
    Channel channel = connection.createChannel();

    channel.exchangeDeclare(EXCHANGE_NAME, "direct", true);

	for(int i = 0; i < argv.length; i++) {		
		String message = argv[i];
		channel.basicPublish(EXCHANGE_NAME, "hola", null, message.getBytes("UTF-8"));
		System.out.println(" [x] Sent: '" + message + "'");
	}


    channel.close();
    connection.close();
  }
  
  
}