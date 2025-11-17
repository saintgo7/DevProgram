// Axis Mapping

#include "Program010.h"

AProgram010::AProgram010()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram010::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Axis Mapping ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating axis mapping."));

    // Implement the program logic here...
}

void AProgram010::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
