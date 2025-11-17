// USkeletalMeshComponent
// Program 020

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program020.generated.h"

UCLASS()
class AProgram020 : public AActor
{
    GENERATED_BODY()

public:
    AProgram020();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
