// Apply Damage

#include "Program044.h"

AProgram044::AProgram044()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram044::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Apply Damage ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating apply damage."));

    // Implement the program logic here...
}

void AProgram044::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
