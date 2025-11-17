// Open Level

#include "Program057.h"

AProgram057::AProgram057()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram057::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Open Level ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating open level."));

    // Implement the program logic here...
}

void AProgram057::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
