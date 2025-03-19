<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
             xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
             xmlns:vm="clr-namespace:WeatherApp.ViewModels"
             xmlns:m="clr-namespace:WeatherApp.Models"
             mc:Ignorable="d" d:DesignWidth="800" d:DesignHeight="450"
             x:Class="WeatherApp.Views.WeatherView"
             x:DataType="vm:WeatherViewModel">

    <UserControl.DataTemplates>
        <DataTemplate DataType="m:Weather">
            <Border BorderBrush="Gray" BorderThickness="1" CornerRadius="5" Margin="5">
                <StackPanel Margin="10">
                    <TextBlock Text="{Binding City}" FontWeight="Bold" FontSize="16"/>
                    <TextBlock Text="{Binding Description}" FontStyle="Italic" Margin="0,0,0,5"/>
                    <Image Source="{Binding Icon}" Width="50" Height="50" Margin="0,0,0,5"/>
                    <TextBlock Text="{Binding Temperature}" FontSize="14"/>
                    <TextBlock Text="{Binding FeelsAsTemperature}" FontSize="14" Foreground="Gray"/>
                    <TextBlock Text="{Binding Humidity}" FontSize="14"/>
                    <TextBlock Text="{Binding Pressure}" FontSize="14"/>
                    <TextBlock Text="{Binding WindSpeed}" FontSize="14"/>
                    <TextBlock Text="{Binding WindDirection}" FontSize="14"/>
                    <TextBlock Text="{Binding Cloudiness}" FontSize="14"/>
                    <TextBlock Text="{Binding Rain}" FontSize="14"/>
                    <TextBlock Text="{Binding Snow}" FontSize="14"/>
                    <TextBlock Text="{Binding DateTime}" FontSize="12" Foreground="DarkGray"/>
                </StackPanel>
            </Border>
        </DataTemplate>
    </UserControl.DataTemplates>

    <Grid>                
        <Grid RowDefinitions="1*,5*,2*,2*,2*" ColumnDefinitions="*,*">
            <Grid Grid.Row="0" Grid.ColumnSpan="4">
                <Grid.ColumnDefinitions>
                    <ColumnDefinition Width="6*"/>
                    <ColumnDefinition Width="2*"/>
                </Grid.ColumnDefinitions>
                <TextBox Grid.Column="0" Height="20" Margin="5,0,5,0" Text="{Binding CityInput}" />
                <Grid Grid.Column="2">
                    <Grid.ColumnDefinitions>
                        <ColumnDefinition/>
                        <ColumnDefinition/>
                    </Grid.ColumnDefinitions>
                    <Button Content="Добавить" Grid.Column="0" BorderBrush="Black" Margin="5,0,5,0" Command="{Binding GetWeatherCommand}"/>
                    <Button Content="Обновить" Grid.Column="1" BorderBrush="Black" Command="{Binding UpdateWeatherCommand}"/>
                </Grid>
            </Grid>

            <ScrollViewer Grid.Row="1" Grid.ColumnSpan="4">
                <ItemsControl ItemsSource="{Binding WeatherCollection}">
                    <ItemsControl.ItemsPanel>
                        <ItemsPanelTemplate>
                            <WrapPanel/>
                        </ItemsPanelTemplate>
                    </ItemsControl.ItemsPanel>
                </ItemsControl>
            </ScrollViewer>
        </Grid>
    </Grid>                
</UserControl>
