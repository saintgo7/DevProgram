// Actor
// Program 002

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program002.generated.h"

UCLASS()
class AProgram002 : public AActor
{
    GENERATED_BODY()

public:
    AProgram002();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
