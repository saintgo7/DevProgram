// Take Damage

#include "Program043.h"

AProgram043::AProgram043()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram043::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Take Damage ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating take damage."));

    // Implement the program logic here...
}

void AProgram043::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
