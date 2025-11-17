// Loop Timer

#include "Program028.h"

AProgram028::AProgram028()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram028::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Loop Timer ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating loop timer."));

    // Implement the program logic here...
}

void AProgram028::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
