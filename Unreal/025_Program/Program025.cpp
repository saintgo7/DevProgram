// Blueprint Interface

#include "Program025.h"

AProgram025::AProgram025()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram025::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Blueprint Interface ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating blueprint interface."));

    // Implement the program logic here...
}

void AProgram025::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
