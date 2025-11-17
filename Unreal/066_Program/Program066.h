// Material
// Program 066

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program066.generated.h"

UCLASS()
class AProgram066 : public AActor
{
    GENERATED_BODY()

public:
    AProgram066();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
