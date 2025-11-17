using Xamarin.Forms;

namespace Program002
{
    public class App : Application
    {
        private int count = 0;
        private Label countLabel;

        public App()
        {
            countLabel = new Label
            {
                Text = "0",
                FontSize = 72,
                FontAttributes = FontAttributes.Bold,
                TextColor = Color.Blue,
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
                            Text = "Counter App",
                            FontSize = 32,
                            FontAttributes = FontAttributes.Bold,
                            HorizontalTextAlignment = TextAlignment.Center
                        },
                        countLabel,
                        new StackLayout
                        {
                            Orientation = StackOrientation.Horizontal,
                            Spacing = 15,
                            Children =
                            {
                                new Button
                                {
                                    Text = "-",
                                    WidthRequest = 60,
                                    HeightRequest = 60,
                                    BackgroundColor = Color.FromHex("#2196F3"),
                                    TextColor = Color.White,
                                    Command = new Command(() =>
                                    {
                                        count--;
                                        countLabel.Text = count.ToString();
                                    })
                                },
                                new Button
                                {
                                    Text = "Reset",
                                    WidthRequest = 100,
                                    HeightRequest = 60,
                                    BackgroundColor = Color.FromHex("#F44336"),
                                    TextColor = Color.White,
                                    Command = new Command(() =>
                                    {
                                        count = 0;
                                        countLabel.Text = count.ToString();
                                    })
                                },
                                new Button
                                {
                                    Text = "+",
                                    WidthRequest = 60,
                                    HeightRequest = 60,
                                    BackgroundColor = Color.FromHex("#2196F3"),
                                    TextColor = Color.White,
                                    Command = new Command(() =>
                                    {
                                        count++;
                                        countLabel.Text = count.ToString();
                                    })
                                }
                            }
                        }
                    }
                }
            };
        }
    }
}
