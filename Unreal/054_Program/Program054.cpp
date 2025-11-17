// Game Instance

#include "Program054.h"

AProgram054::AProgram054()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram054::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Game Instance ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating game instance."));

    // Implement the program logic here...
}

void AProgram054::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
