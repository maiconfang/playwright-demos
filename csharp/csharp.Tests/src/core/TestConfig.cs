namespace Core;

/// <summary>
/// Global test settings, like the base URL of the application.
/// </summary>
public static class TestConfig
{
    // Base URL used for all tests
    public static string BaseUrl => "http://localhost:4200";

    // You can add more config constants if needed:
    public static int DefaultTimeout => 5000;

    // Example: public static string LoginPath => "/#/login";
}