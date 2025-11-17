using Xamarin.Forms;

namespace Program001
{
    public class App : Application
    {
        public App()
        {
            MainPage = new ContentPage
            {
                Content = new StackLayout
                {
                    VerticalOptions = LayoutOptions.Center,
                    HorizontalOptions = LayoutOptions.Center,
                    Children =
                    {
                        new Label
                        {
                            Text = "Hello, Xamarin!",
                            FontSize = 32,
                            FontAttributes = FontAttributes.Bold,
                            TextColor = Color.Blue,
                            HorizontalTextAlignment = TextAlignment.Center
                        },
                        new Label
                        {
                            Text = "Welcome to Cross-Platform Development",
                            FontSize = 18,
                            TextColor = Color.Gray,
                            HorizontalTextAlignment = TextAlignment.Center,
                            Margin = new Thickness(0, 10, 0, 0)
                        }
                    }
                }
            };
        }
    }
}
