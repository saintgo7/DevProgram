// Game Mode

#include "Program051.h"

AProgram051::AProgram051()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram051::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Game Mode ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating game mode."));

    // Implement the program logic here...
}

void AProgram051::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
