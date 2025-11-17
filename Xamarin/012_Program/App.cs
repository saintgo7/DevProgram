using Xamarin.Forms;

namespace Program012
{
    public class App : Application
    {
        private bool isActive = false;
        private Label statusLabel;

        public App()
        {
            statusLabel = new Label
            {
                Text = "Inactive",
                FontSize = 24,
                TextColor = Color.Red,
                HorizontalTextAlignment = TextAlignment.Center
            };

            MainPage = new ContentPage
            {
                Content = new StackLayout
                {
                    VerticalOptions = LayoutOptions.Center,
                    HorizontalOptions = LayoutOptions.Center,
                    Spacing = 20,
                    Children =
                    {
                        new Label
                        {
                            Text = "Xamarin Program 012",
                            FontSize = 28,
                            FontAttributes = FontAttributes.Bold,
                            HorizontalTextAlignment = TextAlignment.Center
                        },
                        statusLabel,
                        new Button
                        {
                            Text = "Toggle",
                            BackgroundColor = Color.FromHex("#2196F3"),
                            TextColor = Color.White,
                            Command = new Command(() =>
                            {
                                isActive = !isActive;
                                statusLabel.Text = isActive ? "Active" : "Inactive";
                                statusLabel.TextColor = isActive ? Color.Green : Color.Red;
                            })
                        }
                    }
                }
            };
        }
    }
}
