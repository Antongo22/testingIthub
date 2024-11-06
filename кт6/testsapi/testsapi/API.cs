using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

public class UserModel
{
    public long Id { get; set; }
    public string Username { get; set; }
    public string FirstName { get; set; }
    public string LastName { get; set; }
    public string Email { get; set; }
    public string Password { get; set; }
    public string Phone { get; set; }
    public int UserStatus { get; set; }
}

public class OrderModel
{
    public long Id { get; set; } 
    public long PetId { get; set; }
    public int Quantity { get; set; }
    public string ShipDate { get; set; }
    public string Status { get; set; }
    public bool Complete { get; set; }
}

public class PetStoreClient
{
    private readonly HttpClient _httpClient;
    private const string BaseUrl = "https://petstore.swagger.io/v2";

    public PetStoreClient()
    {
        _httpClient = new HttpClient();
    }

    public async Task<HttpResponseMessage> CreateUserAsync(UserModel user)
    {
        var json = JsonConvert.SerializeObject(user);
        var content = new StringContent(json, Encoding.UTF8, "application/json");
        return await _httpClient.PostAsync($"{BaseUrl}/user", content);
    }

    public async Task<HttpResponseMessage> GetUserAsync(string username)
    {
        return await _httpClient.GetAsync($"{BaseUrl}/user/{username}");
    }

    public async Task<HttpResponseMessage> CreateOrderAsync(OrderModel order)
    {
        var json = JsonConvert.SerializeObject(order);
        var content = new StringContent(json, Encoding.UTF8, "application/json");
        return await _httpClient.PostAsync($"{BaseUrl}/store/order", content);
    }

    public async Task<HttpResponseMessage> GetOrderAsync(long orderId)
    {
        return await _httpClient.GetAsync($"{BaseUrl}/store/order/{orderId}");
    }

    public async Task<HttpResponseMessage> DeleteOrderAsync(long orderId)
    {
        return await _httpClient.DeleteAsync($"{BaseUrl}/store/order/{orderId}");
    }
}