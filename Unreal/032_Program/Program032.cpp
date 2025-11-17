// Animation Instance

#include "Program032.h"

AProgram032::AProgram032()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram032::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Animation Instance ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating animation instance."));

    // Implement the program logic here...
}

void AProgram032::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
