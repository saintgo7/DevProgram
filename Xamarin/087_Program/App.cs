using System;
using Xamarin.Forms;

namespace Program087
{
    public class App : Application
    {
        public App()
        {
            var box = new BoxView
            {
                Color = Color.FromHex("#2196F3"),
                WidthRequest = 100,
                HeightRequest = 100,
                HorizontalOptions = LayoutOptions.Center
            };

            bool isAnimating = true;
            Device.StartTimer(TimeSpan.FromMilliseconds(16), () =>
            {
                if (isAnimating)
                {
                    box.RotateTo(360, 2000);
                    Device.StartTimer(TimeSpan.FromSeconds(2), () =>
                    {
                        box.Rotation = 0;
                        return false;
                    });
                }
                return true;
            });

            MainPage = new ContentPage
            {
                Content = new StackLayout
                {
                    VerticalOptions = LayoutOptions.Center,
                    Spacing = 30,
                    Children =
                    {
                        new Label
                        {
                            Text = "Advanced 087",
                            FontSize = 28,
                            FontAttributes = FontAttributes.Bold,
                            HorizontalTextAlignment = TextAlignment.Center
                        },
                        box,
                        new Button
                        {
                            Text = "Toggle Animation",
                            BackgroundColor = Color.FromHex("#4CAF50"),
                            TextColor = Color.White,
                            Command = new Command(() =>
                            {
                                isAnimating = !isAnimating;
                            })
                        }
                    }
                }
            };
        }
    }
}
