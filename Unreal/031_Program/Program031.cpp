// Animation Blueprint

#include "Program031.h"

AProgram031::AProgram031()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram031::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Animation Blueprint ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating animation blueprint."));

    // Implement the program logic here...
}

void AProgram031::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
