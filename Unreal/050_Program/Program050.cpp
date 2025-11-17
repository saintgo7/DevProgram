// Main Menu

#include "Program050.h"

AProgram050::AProgram050()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram050::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Main Menu ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating main menu."));

    // Implement the program logic here...
}

void AProgram050::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
