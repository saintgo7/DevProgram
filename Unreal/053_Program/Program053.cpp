// Player State

#include "Program053.h"

AProgram053::AProgram053()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram053::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Player State ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating player state."));

    // Implement the program logic here...
}

void AProgram053::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
