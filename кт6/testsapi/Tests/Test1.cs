using System.Net.Http;
using System.Threading.Tasks;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Newtonsoft.Json;
using System.Threading;

[TestClass]
public class PetStoreTests
{
    private PetStoreClient _client;

    [TestInitialize]
    public void Setup()
    {
        _client = new PetStoreClient();
    }

    [TestMethod]
    [TestCategory("User Management")]
    [Description("Create and retrieve a user")]
    public async Task TestCreateUser()
    {
        var user = new UserModel
        {
            Id = 0,
            Username = "string",
            FirstName = "string",
            LastName = "string",
            Email = "string",
            Password = "string",
            Phone = "string",
            UserStatus = 0
        };

        var createResponse = await _client.CreateUserAsync(user);
        Assert.AreEqual(200, (int)createResponse.StatusCode, "User creation failed");

        Thread.Sleep(1000); 

        var getResponse = await _client.GetUserAsync(user.Username);
        Assert.AreEqual(200, (int)getResponse.StatusCode, "User not found after creation");

        var getUser = JsonConvert.DeserializeObject<UserModel>(await getResponse.Content.ReadAsStringAsync());
        Assert.AreEqual(user.Username, getUser.Username, "User data mismatch");
    }

    [TestMethod]
    [TestCategory("Order Management")]
    [Description("Retrieve an order")]
    public async Task TestGetOrder()
    {
        var order = new OrderModel
        {
            Id = 12,
            PetId = 0,
            Quantity = 0,
            ShipDate = "2024-11-06T13:14:15.369Z",
            Status = "placed",
            Complete = true
        };

        var createResponse = await _client.CreateOrderAsync(order);
        Assert.AreEqual(200, (int)createResponse.StatusCode, "Order creation failed");

        Thread.Sleep(1000); 

        var getResponse = await _client.GetOrderAsync(order.Id);
        Assert.AreEqual(200, (int)getResponse.StatusCode, "Order not found");

        var getOrder = JsonConvert.DeserializeObject<OrderModel>(await getResponse.Content.ReadAsStringAsync());
        Assert.AreEqual(order.Status, getOrder.Status, "Order status mismatch");
    }

    [TestMethod]
    [TestCategory("Order Management")]
    [Description("Delete an order")]
    public async Task TestDeleteOrder()
    {
        var order = new OrderModel
        {
            Id = 12,
            PetId = 0,
            Quantity = 0,
            ShipDate = "2024-11-06T13:14:15.369Z",
            Status = "placed",
            Complete = true
        };

        var createResponse = await _client.CreateOrderAsync(order);
        Assert.AreEqual(200, (int)createResponse.StatusCode, "Order creation failed");

        var deleteResponse = await _client.DeleteOrderAsync(order.Id);
        Assert.AreEqual(200, (int)deleteResponse.StatusCode, "Failed to delete order");

        var getResponse = await _client.GetOrderAsync(order.Id);
        Assert.AreEqual(404, (int)getResponse.StatusCode, "Order still exists after deletion");
    }
}