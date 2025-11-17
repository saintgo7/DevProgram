// Enhanced Input
// Program 007

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program007.generated.h"

UCLASS()
class AProgram007 : public AActor
{
    GENERATED_BODY()

public:
    AProgram007();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
