// Multiplayer

#include "Program092.h"

AProgram092::AProgram092()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram092::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Multiplayer ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating multiplayer."));

    // Implement the program logic here...
}

void AProgram092::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
