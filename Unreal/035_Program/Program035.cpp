// Animation Notify

#include "Program035.h"

AProgram035::AProgram035()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram035::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Animation Notify ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating animation notify."));

    // Implement the program logic here...
}

void AProgram035::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
