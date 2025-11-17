// Material

#include "Program066.h"

AProgram066::AProgram066()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram066::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Material ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating material."));

    // Implement the program logic here...
}

void AProgram066::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
